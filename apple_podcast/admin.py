from django.contrib import admin

from django.contrib.auth.models import User, Group
from .models import PodcastAdmin, Podcast

# Register your models here.
admin.site.register(Podcast, PodcastAdmin)

# Clean useless model
admin.site.unregister(User)
admin.site.unregister(Group)
