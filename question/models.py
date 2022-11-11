from django.db import models
from django.utils.translation import gettext_lazy as _


def qids():
    return BasicQuestion.objects.count() + 1


def aqids():
    return AdvancedQuestion.objects.count() + 1


class Question(models.Model):
    qid = models.IntegerField(_("题号"), default=0, null=False, blank=True)
    question = models.CharField(_("题目"), max_length=128)
    order = models.BooleanField(_("选项正序"), default=True)

    class Meta:
        abstract = True
        verbose_name = _("题库")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class BasicQuestion(Question):
    qid = models.IntegerField(_("题号"), default=qids, null=False, blank=True)

    class Meta:
        verbose_name = _("基础题库")
        verbose_name_plural = verbose_name


class AdvancedQuestion(Question):
    qid = models.IntegerField(_("题号"), default=aqids, null=False, blank=True)

    class Meta:
        verbose_name = _("进阶题库")
        verbose_name_plural = verbose_name
