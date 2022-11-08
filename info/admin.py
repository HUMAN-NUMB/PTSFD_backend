from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from info.models import Info


class InfoAdmin(BaseUserAdmin):
    list_display = ("user_id", "sex", "birthday", "area", "contact", "introduction")
    list_filter = ("user_id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user_id",
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
                    "user_id",
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
    search_fields = ("user_id",)
    ordering = ("user_id",)
    filter_horizontal = ()


admin.site.register(Info, InfoAdmin)
