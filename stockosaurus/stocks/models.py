from django.db import models


class StockPrice(models.Model):
	id = models.IntegerField(primary_key=True, default=0)
	price = models.FloatField()
	time = models.DateTimeField()
	ticker_symbol = models.TextField()
	# owner = models.ForeignKey('auth.User', related_name='StockPrice', on_delete=models.CASCADE, default=None)

	class Meta:
		ordering = ['time']


class NasdaqDaily(models.Model):
	id = models.IntegerField(primary_key=True, default=0)
	date = models.DateTimeField()
	open = models.FloatField()
	high = models.FloatField()
	low = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()
	ticker = models.TextField()

	class Meta:
		ordering = ['date']
