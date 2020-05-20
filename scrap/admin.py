from django.contrib import admin

from django.contrib.auth.models import User, Group
from .models import Bike, BikeAdmin

# Register your models here.
admin.site.register(Bike, BikeAdmin)

# Clean useless model
admin.site.unregister(User)
admin.site.unregister(Group)
