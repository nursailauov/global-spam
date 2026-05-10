"""Vercel Serverless Function entrypoint.

The main bot in app.py is a long-running TCP/async process. Vercel Functions are
request/response based, so this lightweight endpoint lets the repository be
connected to Vercel and deployed successfully without starting the bot at import
time.
"""

from http.server import BaseHTTPRequestHandler
import json
import os
from datetime import datetime, timezone


class handler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send_json(
            200,
            {
                "ok": True,
                "service": "global-spam",
                "runtime": "vercel-python",
                "time": datetime.now(timezone.utc).isoformat(),
                "note": (
                    "Vercel deployment is ready. The bot itself is a persistent "
                    "TCP worker and should be run on a VPS/container, not inside "
                    "a short-lived Vercel Function."
                ),
                "bot_accounts_configured": bool(os.environ.get("BOT_ACCOUNTS_JSON")),
            },
        )

    def do_POST(self):
        self._send_json(
            405,
            {
                "ok": False,
                "error": "method_not_allowed",
                "message": "This Vercel endpoint is a health/status endpoint only.",
            },
        )
