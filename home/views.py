from django.shortcuts import render, redirect
from .models import feed
from user.models import User
from .forms import AnswerForm
# Create your views here.

def test(request):
	return render(request, 'home/index.html')

def feeds_home(request):
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

	print(request.method)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print(form)
		if form.is_valid():
			form.instance.from_user = request.user
			form.save()
			# return redirect('feeds')
	else:
		form = AnswerForm()
	feeds   = feed.objects.all()
	context = {
		'form' : form,
		'feeds'	 : feeds,
	}
	return render(request, 'home/feeds.html', context)