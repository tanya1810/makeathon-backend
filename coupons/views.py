from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.utils.crypto import get_random_string

# Create your views here.
def available(request, id=None):
	user = request.user
	if id:
		coupon = AvailableCoupons.objects.get(id=id)
		if user.coins <= coupon.cost:
			messages.add_message(request, messages.INFO, 'You don\'t have enough coins to buy.')
		else:
			unique_code = get_random_string(length=8)

			Purchased = PurchasedCoupons.objects.create(coupon=coupon, unique_code=unique_code, owner=user)
			user.coins = user.coins - coupon.cost
			print(user.coins)
			user.save()
	coupons = AvailableCoupons.objects.order_by('-id')
	user = request.user

	context = {
		'coupons' : coupons,
	}
	return render(request, 'coupons/available_coupons.html', context)

def purchased(request, id=None):
	coupons = PurchasedCoupons.objects.filter(owner=request.user)
	context = {
		'coupons': coupons,
	}
	return render(request, 'coupons/purchased_coupons.html', context)

def issued_coupons(request, pk = None):	
	issued = PurchasedCoupons.objects.filter(coupon__company=request.user)

	if pk:
		to_del = issued.filter(id=pk)
		to_del.delete()


	context = {
		'issued': issued,
	}
	return render(request, 'coupons/issued.html', context)
def dashboard(request):
	return render(request, 'coupons/dashboard.html')
