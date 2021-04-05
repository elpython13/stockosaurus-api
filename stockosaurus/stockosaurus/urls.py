from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.urls import path, include


urlpatterns = [
    path('', include('stocks.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
