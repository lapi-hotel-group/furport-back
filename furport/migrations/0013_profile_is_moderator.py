# Generated by Django 3.0.8 on 2020-07-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("furport", "0012_auto_20200711_0659"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_moderator",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="モデレータフラグ"
            ),
        ),
    ]
