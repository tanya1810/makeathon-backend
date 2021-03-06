from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('resources/', all_resources, name='all-resources'),
    path('new/resource/', post_resource, name='post_resource'),
    path('like/<int:pk>/', like_resource, name='like_resource'),
    path('dislike/<int:pk>/', dislike_resource, name='like_resource'),
    path('update/resource/<int:pk>/', update_resource, name='update_resource'),
    path('delete/<int:pk>/', delete_resource, name='delete_resource'),
    path('my/posted/resources/', my_posted_resources, name='my_posted_resources'),
    path('my/bought/resources/', my_bought_resources, name='my_bought_resources'),
]
