from django import forms
from .models import Room, RoomObject

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'icon']

class RoomObjectForm(forms.ModelForm):
    class Meta:
        model = RoomObject
        fields = ['room', 'object_name', 'pdf_file']