# Generated by Django 4.1.3 on 2022-11-11 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import info.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Info",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="info",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
                ("nickname", models.CharField(max_length=128, verbose_name="昵称")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=info.models.rename_picture,
                        verbose_name="头像",
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("男", "可爱的男孩纸"),
                            ("女", "呵，女人，你引起我的主意了"),
                            ("权限狗", "至高之人"),
                        ],
                        max_length=5,
                        null=True,
                        verbose_name="性别",
                    ),
                ),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="生日"),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True, max_length=1024, null=True, verbose_name="个性签名"
                    ),
                ),
                (
                    "contact",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="联系方式"
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="地区"
                    ),
                ),
            ],
            options={
                "verbose_name": "信息",
                "verbose_name_plural": "信息",
            },
        ),
    ]
