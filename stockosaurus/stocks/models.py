from django.db import models


class StockPrice(models.Model):
	price = models.FloatField()
	time = models.DateTimeField()
	ticker_symbol = models.TextField()

	class Meta:
		ordering = ['time']
