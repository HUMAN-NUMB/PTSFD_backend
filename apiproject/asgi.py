"""
ASGI config for api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os, django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chat.consumers import ChatConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiproject.settings")
django.setup()
application = ProtocolTypeRouter(
    {
        # websocket请求使用这个
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/chat", ChatConsumer.as_asgi()),
                ]
            )
        ),
    }
)