# Generated by Django 4.1.3 on 2022-11-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Info",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="favicon/%Y/%m/%d/"
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        blank=True,
                        choices=[("m", "男"), ("f", "女")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("birthday", models.DateField(blank=True, null=True)),
                (
                    "introduction",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("contact", models.CharField(blank=True, max_length=20, null=True)),
                ("area", models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]