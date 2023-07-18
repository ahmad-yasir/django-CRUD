from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('join/', views.join, name="join"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),
    path('edit/<event_id>', views.edit, name="edit"),

]


