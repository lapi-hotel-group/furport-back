from django.contrib import admin
from furport.models import Event, Tag, TagGroup, Profile

admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(TagGroup)
admin.site.register(Profile)
