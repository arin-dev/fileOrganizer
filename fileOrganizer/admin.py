from django.contrib import admin

# Register your models here.
from .models import Room, RoomObject

admin.site.register(Room)
admin.site.register(RoomObject)