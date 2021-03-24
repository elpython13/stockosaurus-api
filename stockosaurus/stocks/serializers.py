from rest_framework import serializers

from stockosaurus.stocks.models import StockPrice


class StockPriceSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	price = serializers.FloatField()
	time = serializers.DateTimeField()
	ticker_symbol = serializers.CharField()

	def create(self, validated_data):
		return StockPrice.object.create(**validated_data)

	def update(self, instance, validated_data):
		instance.price = validated_data.get('price', instance.price)
		instance.time = validated_data.get('time', instance.price)
		instance.ticker_symbol = validated_data.get('ticker_symbol', instance.price)
		instance.save()
		return instance
