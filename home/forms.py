from .models import *
from django import forms

class AnswerForm(forms.ModelForm):
	class Meta():
		model = Feed
		fields = ['title', 'post_type', 'description', 'image']