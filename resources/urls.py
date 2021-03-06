from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('resources/', all_resources, name='all-resources'),
    path('new/resource/', post_resource, name='post_resource'),
]
