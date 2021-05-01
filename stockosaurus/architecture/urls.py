from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('architecture/', views.api_root),
    path('', views.api_root),

]
urlpatterns = format_suffix_patterns(urlpatterns)
