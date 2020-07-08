# Generated by Django 3.0.8 on 2020-07-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("furport", "0003_auto_20200708_0528"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="city",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="市名"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="country",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="国名"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="place",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="会場名"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="state",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="都道府県・州名"
            ),
        ),
    ]
