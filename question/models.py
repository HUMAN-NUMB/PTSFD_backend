from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Question(models.Model):
    id = models.BigAutoField(_("题号"), primary_key=True, editable=False)
    question = models.CharField(_("题目"), max_length=128)
    order = models.BooleanField(_("选项正序"), default=True)

    class Meta:
        verbose_name = _("题库")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question
