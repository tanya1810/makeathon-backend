from django.shortcuts import render
from django.shortcuts import render, redirect

def test(request):
	return render(request, 'home/base.html')

def test1(request):
	return render(request, 'home/portfolio-details.html')