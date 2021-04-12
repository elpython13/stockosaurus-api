from rest_framework import serializers
from .models import StockPrice, NasdaqDaily


class StockPriceSerializer(serializers.HyperlinkedModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = StockPrice
		fields = ['id', 'price', 'time', 'ticker_symbol']

	def create(self, validated_data):
		return StockPrice.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.price = validated_data.get('price', instance.price)
		instance.time = validated_data.get('time', instance.price)
		instance.ticker_symbol = validated_data.get('ticker_symbol', instance.price)
		instance.save()
		return instance


class NasdaqDailySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = NasdaqDaily
		fields = ['id', 'date', 'open', 'high', 'low', 'close', 'volume', 'ticker']

	def create(self, validated_data):
		return NasdaqDaily.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.date = validated_data.get('date', instance.price)
		instance.open = validated_data.get('open', instance.price)
		instance.high = validated_data.get('high', instance.price)
		instance.low = validated_data.get('low', instance.price)
		instance.close = validated_data.get('close', instance.price)
		instance.volume = validated_data.get('volume', instance.price)
		instance.ticker = validated_data.get('ticker', instance.price)
		instance.save()
		return instance
