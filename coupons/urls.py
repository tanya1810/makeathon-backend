from django.urls import path
from . import views

urlpatterns = [
    path('available/',			views.available,		name='feeds'),
    # path('test1/',            views.test1,     name='test1'),
]
