from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.utils.crypto import get_random_string

# Create your views here.
def available(request, id=None):
	user = request.user

	# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# print(coupon)
	# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	if id:
		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		coupon = AvailableCoupons.objects.get(id=id)
		if user.coins <= coupon.cost:
			messages.add_message(request, messages.INFO, 'You don\'t have enough coins to buy.')
		else:
			unique_code = get_random_string(length=8)

			Purchased = PurchasedCoupons.objects.create(coupon=coupon, unique_code=unique_code, owner=user)
			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			print(user.coins)
			user.coins = user.coins - coupon.cost
			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			print(user.coins)
			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			user.save()



	coupons = AvailableCoupons.objects.order_by('-id')
	user = request.user

	context = {
		'coupons' : coupons,
	}
	return render(request, 'coupons/available_coupons.html', context)