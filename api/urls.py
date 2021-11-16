from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .views import CarView


app_name = 'api'
urlpatterns = [
    path('cars/', CarView.as_view(), name='cars'),
]