from django.db import models

# Create your models here.
class feed(models.Model):
# - from(user)
# - video(not req)
	post_type = (('Doubt', 'Doubt'),
				('News', 'News'),)

	head = models.CharField(max_length=50)
	post_type = models.CharField(choices=post_type, max_length=5)
	text = models.CharField(max_length=500)
	image = models.ImageField(default='feed/default.jpg', upload_to='feed/')    

	def __str__(self):
		return self.head