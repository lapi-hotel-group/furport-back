from django.contrib import admin
from furport.models import Event, GeneralTag, CharacterTag, OrganizationTag, Profile

admin.site.register(Event)
admin.site.register(GeneralTag)
admin.site.register(CharacterTag)
admin.site.register(OrganizationTag)
admin.site.register(Profile)
