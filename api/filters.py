from django_filters import rest_framework as filters
from .models import Car

class CarFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    price = filters.NumberFilter(field_name='price')

    class Meta:
        model = Car
        fields = ('name', 'price')