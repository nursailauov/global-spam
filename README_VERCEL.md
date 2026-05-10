# Deploy to Vercel

Этот репозиторий теперь можно подключить к Vercel как Python Serverless Function.

## Что добавлено

- `api/index.py` — HTTP health/status endpoint для Vercel.
- `vercel.json` — маршруты `/`, `/health`, `/status` перенаправляются на `/api`.
- `.python-version` — фиксирует Python `3.12`, который поддерживается Vercel.
- `requirements.txt` — оставлен без зависимостей, потому что Vercel endpoint использует только стандартную библиотеку.
- `.vercelignore` — не отправляет кэш, локальные env-файлы и `vv.json` в Vercel.

## Как подключить

1. Залей репозиторий в GitHub/GitLab/Bitbucket.
2. В Vercel нажми **Add New Project**.
3. Выбери этот репозиторий.
4. Framework Preset можно оставить **Other**.
5. Build Command оставь пустым.
6. Deploy.

После деплоя открой:

- `/` — статус endpoint.
- `/health` — health-check endpoint.
- `/status` — status endpoint.

## Важное ограничение

Основной `app.py` — это долгоживущий async/TCP bot-worker. Vercel Functions работают как короткие HTTP request/response функции, поэтому они не подходят для постоянного запуска такого бота.

Vercel в этом репозитории используется для HTTP status/health endpoint и проверки, что проект деплоится. Самого бота лучше запускать на VPS, Docker, Render Worker, Railway Worker или другом сервисе, который поддерживает постоянный процесс.

## Секреты

Не загружай реальные аккаунты в `vv.json` на Vercel. Для Vercel используй Environment Variables. Endpoint уже проверяет наличие переменной `BOT_ACCOUNTS_JSON`, но не читает и не запускает аккаунты внутри serverless-функции.
