from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount

from furport.models import Profile


@receiver(post_save, sender=SocialAccount)
def socialAccountSaveHandler(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.user)
        profile.avatar = instance.get_avatar_url()
        profile.save(update_fields=["avatar"])
