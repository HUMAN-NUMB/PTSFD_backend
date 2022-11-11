from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from hashlib import md5
import os


User = get_user_model()


def rename_picture(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{md5(instance.user.username.encode()).hexdigest()[:10]}.{ext}"
    return os.path.join(instance.user.username, filename)


class Info(models.Model):
    SEX_CHOICES = (("男", _("可爱的男孩纸")), ("女", _("呵，女人，你引起我的主意了")), ("权限狗", _("至高之人")))

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="info",
        primary_key=True,
        verbose_name=_("用户"),
    )
    nickname = models.CharField(_("昵称"), max_length=128, null=False, blank=False)
    image = models.ImageField(_("头像"), upload_to=rename_picture, null=True, blank=True)
    sex = models.CharField(
        _("性别"), max_length=5, choices=SEX_CHOICES, null=True, blank=True
    )
    birthday = models.DateField(_("生日"), null=True, blank=True)
    introduction = models.TextField(_("个性签名"), max_length=1024, null=True, blank=True)
    contact = models.CharField(_("联系方式"), max_length=128, null=True, blank=True)
    area = models.CharField(_("地区"), max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = _("信息")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_extension_user(sender, instance, created, **kwargs):
    if created:
        Info.objects.create(user=instance, nickname=instance.username)
    else:
        instance.info.save()
