from django.contrib import admin

from question.models import BasicQuestion, AdvancedQuestion


@admin.register(BasicQuestion)
@admin.register(AdvancedQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "qid",
        "question",
        "order",
    )
    list_filter = ("qid",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "question",
                    "qid",
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
                    "qid",
                    "order",
                ),
            },
        ),
    )
    search_fields = ("qid",)
    ordering = ("qid",)
    filter_horizontal = ()
