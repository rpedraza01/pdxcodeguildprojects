import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class GroceryItem(models.Model):
	item_description_text = models.CharField(max_length=200)
	created_date = models.DateTimeField('date created')
	completed_date = models.DateTimeField(null=True, blank=True)
	item_was_completed = models.BooleanField(default=False)


	def __str__(self):
		return self.item_description_text