from datetime import date
from django.db import models

# Create your models here.
class User(models.Model):
    SEX_CHOICES = [("m", "男"), ("f", "女")]

    name = models.CharField("用户名", max_length=20, unique=True)
    password = models.CharField("密码哈希", max_length=32)

    image = models.ImageField(
        "头像", upload_to="favicon/%Y/%m/%d/", null=True, blank=True
    )
    sex = models.CharField("性别", max_length=1, choices=SEX_CHOICES, blank=True)
    birthday = models.DateField("生日", default=date.today)
    introduction = models.CharField("简介", max_length=500, blank=True)
    contact = models.CharField("联系方式", max_length=20, blank=True)
    area = models.CharField("地区", max_length=20, blank=True)

    def __str__(self):
        return self.name
