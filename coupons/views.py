from django.shortcuts import render

# Create your views here.
def available(request):
	return render(request, 'coupons/available_coupons.html')