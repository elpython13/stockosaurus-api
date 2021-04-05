from rest_framework import serializers
from .models import StockPrice


class StockPriceSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = StockPrice
		fields = ['id', 'price', 'time', 'ticker_symbol', 'owner']

	def create(self, validated_data):
		return StockPrice.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.price = validated_data.get('price', instance.price)
		instance.time = validated_data.get('time', instance.price)
		instance.ticker_symbol = validated_data.get('ticker_symbol', instance.price)
		instance.save()
		return instance

