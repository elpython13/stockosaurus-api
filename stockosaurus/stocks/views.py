from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import StockPrice
from .serializers import StockPriceSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'stocks': reverse('stock-list', request=request, format=format),
		'tickers': reverse('ticker-list', request=request, format=format),
	})


class StockList(generics.ListAPIView):
	serializer_class = StockPriceSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def get_queryset(self):
		queryset = StockPrice.objects.all()
		ticker = self.request.query_params.get('ticker')
		start = self.request.query_params.get('start')
		end = self.request.query_params.get('end')

		if ticker is not None:
			queryset = queryset.filter(ticker_symbol=str(ticker).upper())

		if start is not None:
			queryset = queryset.filter(time__gte=start)

		if end is not None:
			queryset = queryset.filter(time__lte=end)

		return queryset


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = StockPrice.objects.all()
	serializer_class = StockPriceSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TickerList(generics.ListAPIView):
	queryset = StockPrice.objects.order_by('ticker_symbol').distinct('ticker_symbol')
	serializer_class = StockPriceSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

