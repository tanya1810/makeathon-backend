from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import feed
# Create your views here.

def test(request):
	return render(request, 'home/index.html')

def feeds_home(request):
	return render(request, 'home/feeds.html')