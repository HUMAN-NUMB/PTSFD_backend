from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from info.models import Info


class InfoAdmin(BaseUserAdmin):
    list_display = ("user", "sex", "birthday", "area", "contact", "introduction")
    list_filter = ("user",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
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
# admin.site.unregister(Group)
