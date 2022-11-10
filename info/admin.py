from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from info.models import Info


admin.site.site_header = "用户信息"
admin.site.site_title = admin.site.site_header
admin.site.index_title = admin.site.site_title


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
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
