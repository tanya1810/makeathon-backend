from django.urls import path
from . import views

urlpatterns = [
    path('test/',				views.test,				name='test'),
    path('feeds/',				views.feeds_home,		name='feeds'),
    # path('test1/',            views.test1,     name='test1'),
]
