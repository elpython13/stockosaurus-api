from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import StockPrice
from .serializers import StockPriceSerializer, UserSerializer
from . permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'stocks': reverse('stock-list', request=request, format=format)
    })


class StockList(generics.ListAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

