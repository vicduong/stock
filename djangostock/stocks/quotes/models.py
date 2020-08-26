from django.db import models

# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=10) # datatype zip code number text char - length

	def __str__(self):
		return self.ticker # register this model in admin area

	# 2 steps: create model here - push it to the database