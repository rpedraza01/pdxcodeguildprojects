from django.db import models

# Create your models here.
class ShortURLs(models.Model):
	long_url = models.CharField(max_length=400)
	short_code = models.CharField(max_length=6)
	number_of_clicks = models.IntegerField(default=0)

	def __str__(self):
		return self.short_code