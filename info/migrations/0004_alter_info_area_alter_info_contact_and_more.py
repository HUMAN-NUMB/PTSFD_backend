# Generated by Django 4.1.3 on 2022-11-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0003_alter_info_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="area",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="info",
            name="contact",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="info",
            name="introduction",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
