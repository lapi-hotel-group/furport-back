# Generated by Django 3.0.8 on 2020-07-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("furport", "0015_profile_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="twitter_id",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="TwitterID"
            ),
        ),
    ]
