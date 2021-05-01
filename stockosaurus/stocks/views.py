from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import NasdaqDaily
from .serializers import NasdaqDailySerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'stocks': reverse('stock-list', request=request, format=format),
	})


class NasdaqDailyList(generics.ListAPIView):
	serializer_class = NasdaqDailySerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def get_queryset(self):
		queryset = NasdaqDaily.objects.all()
		ticker = self.request.query_params.get('ticker')

		if ticker is not None:
			queryset = queryset.filter(ticker=str(ticker).upper())
		
		return queryset
