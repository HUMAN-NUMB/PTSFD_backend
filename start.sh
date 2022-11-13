#!/bin/bash

daphne -b 127.0.0.1 -p 8000 --proxy-headers apiproject.asgi:application &
daphne -b 127.0.0.1 -p 8001 --proxy-headers apiproject.asgi:application &
tail -f /dev/null