from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User

from furport.models import Profile


@receiver(post_save, sender=SocialAccount)
def socialAccountSaveHandler(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.user)

        import re

        profile.avatar = re.sub(
            r"^https?://", "https://", instance.get_avatar_url(), count=1
        )
        profile.twitter_id = instance.get_provider_account()

        profile.save(update_fields=["avatar", "twitter_id"])


@receiver(post_save, sender=User)
def userSaveHandler(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
