from django.contrib import admin

from question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question",
        "order",
    )
    list_filter = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "question",
                    "order",
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
                    "question",
                    "order",
                ),
            },
        ),
    )
    search_fields = ("id",)
    ordering = ("id",)
    filter_horizontal = ()
