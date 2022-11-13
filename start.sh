#!/bin/ash

python3 -m gunicorn apiproject.asgi:application -k uvicorn.workers.UvicornWorker
tail -f /dev/null