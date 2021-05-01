from django.db import models


class NasdaqDaily(models.Model):
	id = models.IntegerField(primary_key=True, default=0)
	date = models.DateField()
	open = models.FloatField()
	high = models.FloatField()
	low = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()
	ticker = models.TextField()

	class Meta:
		ordering = ['date']
		
