from channels.auth import AuthMiddlewareStack
from channels.middleware import BaseMiddleware
from django.db import close_old_connections
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken

# from jwt import decode as jwt_decode
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser, User
# from channels.db import database_sync_to_async
# from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPE_BYTES


# @database_sync_to_async
# def get_user(user_id):
#     try:
#         return get_user_model().objects.get(user_id=user_id)
#     except User.DoesNotExist:
#         return AnonymousUser()


class JwtAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Close old database connections to prevent usage of timed out connections
        close_old_connections()
        # Copy scope to stop changes going upstream
        scope = dict(scope)
        # Get the token
        token = scope["query_string"]
        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            print(f"InvaildURL: {e}")
            return None
        # else:
        #     #  Then token is valid, decode it
        #     decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        #     # Will return a dictionary like -
        #     # {
        #     #     "token_type": "access",
        #     #     "exp": 1568770772,
        #     #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
        #     #     "user_id": 6
        #     # }

        #     # Get the user using ID
        #     scope["user"] = await get_user(user_id=decoded_data["user_id"])
        return await self.inner(scope, receive, send)


def JwtAuthMiddlewareStack(inner):
    return JwtAuthMiddleware(AuthMiddlewareStack(inner))
