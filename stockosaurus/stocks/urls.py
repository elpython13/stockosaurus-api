from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('stocks/', views.NasdaqDailyList.as_view(), name='stock-list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
