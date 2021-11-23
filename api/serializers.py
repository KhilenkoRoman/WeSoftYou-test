from rest_framework import serializers
from .models import Car, CarPart


class CarPartSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CarPart
        fields = ('name', 'qty')

class CarSerializer(serializers.ModelSerializer):
    parts = CarPartSerializer(many=True)
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, instance):
        return str(self.context['request'].user)
   
    class Meta:
        model = Car
        fields = ('name', 'description', 'price', 'user', 'parts')


class CarAggregationSerializer(serializers.ModelSerializer):
    parts_qty = serializers.IntegerField()
   
    class Meta:
        model = Car
        fields = ('name', 'price', 'parts_qty')