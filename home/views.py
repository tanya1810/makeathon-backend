from django.shortcuts import render, redirect
from .models import *
from user.models import User
from .forms import AnswerForm

def feeds_home(request):
	print('hello')
	if(request.method == 'POST'):
		form = AnswerForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.from_user = request.user
			form.save()
	
	form = AnswerForm()
	feeds   = Feed.objects.all()
	context = {
		'form' : form,
		'feeds'	 : feeds,
	}
	return render(request, 'home/feeds.html', context)

def feed_details(request, pk):
	feed = Feed.objects.filter(id = pk)
	comment = Comments.objects.filter(feed=feed)
	context = {
		'feed' : feed,
		'comment' : comment
	}
	return render(request, 'home/feeds-single.html')