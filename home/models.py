from django.db import models
from user.models import User

# Create your models here.
class feed(models.Model):
# - video(not req)
	post_type = (('Doubt', 'Doubt'),
				('News', 'News'),)

	from_user 			= models.ForeignKey(User, related_name = 'from_user', on_delete=models.CASCADE, null=False, blank=False)
	head 				= models.CharField(max_length=50)
	post_type			= models.CharField(choices=post_type, max_length=5)
	text 				= models.CharField(max_length=500)
	image 				= models.ImageField(default='feed/default.jpg', upload_to='feed/')    

	def __str__(self):
		return self.head

class comments(object):

	by_user 			= models.ForeignKey(User, related_name= 'by_user', on_delete=models.CASCADE, null=False, blank=False)
	feed 				= models.ForeignKey(feed, related_name= 'feed', on_delete=models.CASCADE, null=True, blank=True)
	text 				= models.CharField(max_length=200, null=False, blank=False)

class request(models.Model):
	year = (('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),)

	from_user 			= models.ForeignKey(User, related_name = 'request_from', on_delete=models.CASCADE, null=False, blank=False)
	subject 			= models.CharField(max_length=50, null=False, blank=False)
	year 				= models.CharField(choices=year, max_length=2)
	description 		= models.CharField(max_length=200)

class resource(models.Model):

# Resource
# - file(hum kisi ki bhi dekh sakte h🥸🥸)
# - sample(plan krna h)
	year = (('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),)


	from_user 			= models.ForeignKey(User, related_name = 'resourse_from', on_delete=models.CASCADE, null=False, blank=False)
	price 				= models.PositiveIntegerField(default=0)
	subject 			= models.CharField(max_length=50, )
	year 				= models.CharField(choices=year, max_length=2)
	description 		= models.CharField(max_length=200)
