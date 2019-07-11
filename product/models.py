from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	url = models.TextField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	votes_total = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__ (self):
		return self.title

class votecount(models.Model):
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)



