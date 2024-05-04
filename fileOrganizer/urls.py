from django.urls import path
from . import views

# from django.conf import settings
# from django.comf.urls.static

# URL CONFIG
urlpatterns = [
    path('hello/', views.testing),
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.object_list, name='object_list'),
    # path('room/<int:room_id>/object/<int:object_id>/', views.object_detail, name='object_detail'),
    # path('create-room/', views.create_room, name='create_room'),
    # path('create-room-object/<int:room_id>/', views.create_room_object, name='create_room_object'),
    # path('room_icons', )
]