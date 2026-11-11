# Konstantinov-NAD-Labs-2026

lab1 — Разработка дизайна приложения и базовая шаблонизация.

Приложение Robolab: каталог команд ROS, лента и форма черновика.
FastAPI + Jinja2, данные в памяти, медиа в Silo.

## Запуск

Нужны Python 3.10+ и работающий Docker Desktop. Из папки проекта в PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
docker compose up -d
.venv\Scripts\python main.py
```

Приложение: http://localhost:8000. Консоль Silo: http://localhost:9001.
Локальный вход в Silo по умолчанию: `localadmin` / `localdevelopment`.
Другие учётные данные задаются через `SILO_ROOT_USER` и `SILO_ROOT_PASSWORD`.
Адрес медиа можно изменить переменной `ROS_MEDIA_BASE`.

При первом запуске откройте консоль Silo, создайте бакет `ros-commands`,
разрешите анонимное чтение (Access Policy: Public) и загрузите в него все
файлы из `media/`, сохранив их имена. На этом компьютере бакет уже настроен.
Для последующих запусков хранилища достаточно `docker compose up -d`.
Остановка: `docker compose stop`; приложение останавливается через Ctrl+C.

Если установленный Docker Desktop сообщает об ошибке версии API,
перед командой Compose выполните `$env:DOCKER_API_VERSION = '1.53'`.

## Структура

```text
api/handlers.py         — три GET-обработчика
data/ros_commands.py   — коллекция команд
templates/             — базовый шаблон и три страницы
static/css/style.css   — стили
static/icons/          — иконки интерфейса
static/fonts/          — шрифт
media/                 — файлы для загрузки в Silo
main.py                — сборка и запуск приложения
requirements.txt       — зависимости
docker-compose.yml     — хранилище Silo
```

## Страницы

- `/` — плитка и фильтр `ros_distance_min` по минимальному расстоянию.
- `/ros-commands/feed` — лента; `ros_command_id` выбирает команду,
  `next=true` открывает следующую опубликованную команду по кругу.
- `/ros-commands/draft` — заполненный черновик без сохранения.

Лайки вычисляются по ID пользователей. БД и JavaScript не используются.
Видео — демонстрационные анимации, а не запись работы настоящего робота.
Макет: https://www.figma.com/design/uAlrAA6EfZhtJ8lYgj2vE0/Untitled
