from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from score.models import Score


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "score",
        "times",
    )
    list_filter = ("user",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "times",
                    "score",
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
                    "times",
                    "score",
                ),
            },
        ),
    )
    search_fields = ("user",)
    ordering = ("user",)
    filter_horizontal = ()
