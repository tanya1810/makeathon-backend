from django.shortcuts import render
from django.shortcuts import render, redirect

def test(request):
	return render(request, 'home/base.html')
# Create your views here.
