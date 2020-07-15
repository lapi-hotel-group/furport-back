# Generated by Django 3.0.8 on 2020-07-15 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("furport", "0014_profile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="follower", to="furport.Profile"
            ),
        ),
    ]