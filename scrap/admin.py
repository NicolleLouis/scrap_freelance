from django.contrib import admin

from django.contrib.auth.models import User, Group
from .models import ItemAdmin, Item

# Register your models here.
admin.site.register(Item, ItemAdmin)

# Clean useless model
admin.site.unregister(User)
admin.site.unregister(Group)
