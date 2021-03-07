from django.urls import path
from . import views

urlpatterns = [
    path('feeds/',				views.feeds_home,		name='feeds'),
    path('feed-details/<int:pk>',				views.feed_details,		name='feed_details'),
]
