from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

urlpatterns = [
    path('admin/', admin.site.urls),
]
