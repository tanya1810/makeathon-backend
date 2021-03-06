from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('resources/', views.all_resources, name='all-resources'),
    path('new/resource/', views.post_resource, name='post_resource'),
]
