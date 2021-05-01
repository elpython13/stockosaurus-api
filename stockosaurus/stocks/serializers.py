from rest_framework import serializers
from .models import NasdaqDaily


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
