from django.urls import path
from . import views

urlpatterns = [
    path('available/',					views.available,		name='available'),
    path('available/<int:id>',			views.available,		name='available'),
    path('purchased/',			views.purchased,		name='purchased'),
    # path('test1/',            views.test1,     name='test1'),
]
