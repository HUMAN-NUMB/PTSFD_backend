from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="score",
        verbose_name=_("用户"),
        null=False,
        blank=True,
    )
    times = models.IntegerField(_("次"), null=False, blank=True)
    score = models.IntegerField(_("分数"), null=False, blank=False)

    class Meta:
        verbose_name = _("分数")
        verbose_name_plural = verbose_name
        ordering = [
            "times",
        ]

    def __str__(self):
        return self.score
