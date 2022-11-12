#!/bin/bash

cd /usr/src/app
uwsgi --ini uwsgi.ini
daphne -b 127.0.0.1 -p 8001 apiproject.asgi:application