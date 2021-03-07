from django.urls import path
from .views import *

urlpatterns = [
    path('feeds/', feeds_home, name='feeds'),
    path('my/feeds/', my_feeds, name='my_feeds'),
    path('delete/feed/<int:id>/', delete_feed, name='delete_feed'),
    path('update/feed/<int:id>/', update_feed, name='update_feed'),
]
