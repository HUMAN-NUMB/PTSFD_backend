from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class Info(models.Model):
    SEX_CHOICES = (("m", "男"), ("f", "女"))

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="info", primary_key=True
    )
    nickname = models.CharField(max_length=128, null=False, blank=False)
    image = models.ImageField(upload_to="favicon/%Y/%m/%d/", null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    introduction = models.CharField(max_length=1024, null=True, blank=True)
    contact = models.CharField(max_length=128, null=True, blank=True)
    area = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_extension_user(sender, instance, created, **kwargs):
    if created:
        Info.objects.create(user=instance, nickname=instance.username)
    else:
        instance.info.save()
