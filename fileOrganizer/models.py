from django.db import models
import os

def get_upload_path_icons(instance, filename):
    return os.path.join('room_icons', filename)

def get_upload_path_pdfs(instance, filename):
    return os.path.join('room_pdfs', filename)

class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to=get_upload_path_icons, blank=True, null=True)

    def __str__(self):
        return self.name

class RoomObject(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=get_upload_path_pdfs, blank=True, null=True)

    def __str__(self):
        return self.object_name