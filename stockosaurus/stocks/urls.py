from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('stocks/', views.StockList.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', views.StockDetail.as_view(), name='stock-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
