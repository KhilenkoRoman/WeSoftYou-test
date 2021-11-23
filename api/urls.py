from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .views import CarView, CarGetView, CarAggregationView, LazyTestView


app_name = 'api'
urlpatterns = [
    path('lazy_test/', LazyTestView.as_view(), name='lazy_test'),
    path('cars/', CarView.as_view(), name='cars'),
    path('get_cars/', CarGetView.as_view(), name='get_cars'),
    path('aggregate_cars/', CarAggregationView.as_view(), name='aggregate_cars'),
]