from django.shortcuts import render
from django.shortcuts import render, redirect

def test(request):
	return render(request, 'home/login.html')
# Create your views here.
