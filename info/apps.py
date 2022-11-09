from django.apps import AppConfig


class InfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "info"

    verbose_name = "用户信息"
