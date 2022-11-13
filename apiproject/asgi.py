"""
ASGI config for api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os, django
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

# from django.core.asgi import get_asgi_application

from chat.consumers import ChatConsumer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiproject.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        # "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        path("ws/chat", ChatConsumer.as_asgi()),
                    ]
                )
            ),
        ),
    }
)
