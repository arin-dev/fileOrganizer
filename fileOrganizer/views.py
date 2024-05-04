from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Room, RoomObject
from .forms import RoomForm, RoomObjectForm

# Create your views here.
#  takes request gives response  

def testing(req):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(req, 'testing.html')

# # CODE FOR DATA MAKING:
# def create_room(request):
#     if request.method == 'POST':
#         form = RoomForm(request.POST, request.FILES)
#         if form.is_valid():
#             room = form.save()
#             return redirect('room_detail', room_id=room.id)
#     else:
#         form = RoomForm()
#     return render(request, 'create_room.html', {'form': form})

# def create_room_object(request, room_id):
#     room = Room.objects.get(id=room_id)
#     if request.method == 'POST':
#         form = RoomObjectForm(request.POST)
#         if form.is_valid():
#             room_object = form.save(commit=False)
#             room_object.room = room
#             room_object.save()
#             return redirect('room_detail', room_id=room_id)
#     else:
#         form = RoomObjectForm(initial={'room': room})
#     return render(request, 'create_room_object.html', {'form': form, 'room': room})

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    room_objects = RoomObject.objects.filter(room=room)
    return render(request, 'room_detail.html', {'room': room, 'room_objects': room_objects})

# CODE FOR DATA RETRIEVAL:
def room_list(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        #     return render(request, 'room_list.html', {'rooms': rooms, 'form': form})
        # else:
        #     # return redirect('room_detail', room_id=room.id)
    form = RoomForm()
    return render(request, 'room_list.html', {'rooms': rooms, 'form': form})

def object_list(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    objects = RoomObject.objects.filter(room=room_id)
    if request.method == 'POST':
        form = RoomObjectForm(request.POST, request.FILES)
        if form.is_valid():
            # room_object = form.save(commit=False)
            room_object = form.save()
            # room_object.room = room
            # room_object.save()
            # return redirect(request, 'object_list.html', {'room': room, 'objects': objects, 'form': form})
    # else:
    form = RoomObjectForm(initial={'room': room})
    return render(request, 'object_list.html', {'room': room, 'objects': objects, 'form': form})

def object_detail(request, room_id, object_id):
    room = get_object_or_404(Room, id=room_id)
    object = get_object_or_404(RoomObject, id=object_id, room=room)
    return render(request, 'object_detail.html', {'room': room, 'object': object})