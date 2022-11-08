from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from info.models import Info


class InfoAdmin(BaseUserAdmin):
    list_display = (
        "user",
        "nickname",
        "sex",
        "birthday",
        "area",
        "contact",
        "introduction",
    )
    list_filter = ("user",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "nickname",
                    "image",
                    "sex",
                    "birthday",
                    "area",
                    "contact",
                    "introduction",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "user",
                    "nickname",
                    "image",
                    "sex",
                    "birthday",
                    "introduction",
                    "contact",
                    "area",
                ),
            },
        ),
    )
    search_fields = ("user",)
    ordering = ("user",)
    filter_horizontal = ()


admin.site.register(Info, InfoAdmin)
