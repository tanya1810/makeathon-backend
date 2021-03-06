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

class comments(models.Model):

	by_user 			= models.ForeignKey(User, related_name= 'by_user', on_delete=models.CASCADE, null=False, blank=False)
	feed 				= models.ForeignKey(feed, related_name= 'feed', on_delete=models.CASCADE, null=True, blank=True)
	text 				= models.CharField(max_length=200, null=False, blank=False)

