from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [
    "admin.your.domain",
    "127.0.0.1",
    "localhost",
]

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "https://*.your.domain",
]

CORS_ALLOW_HEADERS = [
    "advance",
]

SECERT_KEY = "django-insecure-4409-@*h&q!@djthqht!9xk#6-ix#c_b@p-h#(t^%5u9s#%2)6"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if DEBUG:
    ALLOWED_HOSTS += [
        "*",
    ]

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        }
    }

else:
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.mysql",
    #         "NAME": "api",
    #         "HOST": "127.0.0.1",
    #         "PORT": 3306,
    #         "USER": "api",
    #         "PASSWORD": "apiapiapi",
    #     },
    # }

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("127.0.0.1", 6379)],
            },
        },
    }
