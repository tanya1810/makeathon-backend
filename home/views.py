from django.shortcuts import render, redirect
from .models import *
from user.models import User
from .forms import *

def feeds_home(request):
	if(request.method == 'POST'):
		form = AnswerForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
	
	form = AnswerForm()
	feeds   = Feed.objects.all()
	context = {
		'form' : form,
		'feeds'	 : feeds,
	}
	return render(request, 'home/feeds.html', context)

def delete_feed(request, pk):
	feed = Feed.objects.get(id=pk)
	if(request.user == feed.author):
		feed.delete()
	else:
			messages.add_message(request, messages.INFO, 'You are not authorized to delete this feed.')

	return redirect('feeds')

def my_post(request):
	if(request.method == 'POST'):
		form = AnswerForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
	
	form = AnswerForm()
	feeds   = Feed.objects.filter(author=request.user)
	context = {
		'form' : form,
		'feeds'	 : feeds,
	}
	return render(request, 'home/my_feeds.html', context)

def update_feed(request, id=None):
	feed = Feed.objects.get(id=id)
	if request.method == 'POST':
		if(request.user == feed.author):
			form = UpdateFeedForm(request.POST, request.FILES, instance=feed)
			if form.is_valid():
				form.save()
				return redirect('feeds')
		else:
			messages.add_message(request, messages.INFO, 'You are not authorized to edit this feed.')
	form = UpdateFeedForm(instance=feed)
	context = {
		'form' : form,
	}
	return render(request, 'home/update_feed.html', context)


def feed_details(request, pk):
	feed = Feed.objects.get(id = pk)
	comment = Comments.objects.filter(feed=feed)
	
	if(request.method == 'POST'):

		form = AddComment(request.POST)
		if form.is_valid():
			form.instance.by_user = request.user
			form.instance.feed = feed
			form.save()
	form = AddComment()
	context = {
		'feed' : feed,
		'comment' : comment,
		'form' : form,
	}
	return render(request, 'home/feeds-single.html', context)
