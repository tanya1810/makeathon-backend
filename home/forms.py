from .models import feed
from django import forms

class AnswerForm(forms.ModelForm):
	CHOICES = [('Doubt', 'Doubt'),
				('News', 'News')]

	Heading			= forms.CharField(max_length=40, required=True)
	post_type		= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
	text 			= forms.CharField(max_length=500, required=False)
	image 			= forms.ImageField(required=False)

    class Meta: 
        model = feed
        fields = ['head', 'post_type', 'text', 'image']