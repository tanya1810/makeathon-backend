from django.shortcuts import render
from .models import *


# Create your views here.
def available(request):
	coupons = AvailableCoupons.objects.order_by('-id')
	print(coupons)
	context = {
		'coupons' : coupons,
	}
	return render(request, 'coupons/available_coupons.html', context)