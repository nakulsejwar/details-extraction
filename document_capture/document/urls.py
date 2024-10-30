from django.urls import path
from . import views
from .views import extract_aadhar


urlpatterns = [
    path('', views.index, name='index'),
    path('aadhar/', extract_aadhar, name='extract_aadhar'),
]
