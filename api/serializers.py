from rest_framework import serializers
from .models import Car, CarPart


class CarPartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CarPart
        fields = ('name', 'qty')

class CarSerializer(serializers.ModelSerializer):
    parts = CarPartSerializer(many=True)
   
    class Meta:
        model = Car
        fields = ('name', 'description', 'price', 'parts')