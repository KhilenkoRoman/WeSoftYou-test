from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CarSerializer, CarAggregationSerializer
from .models import Car
from rest_framework.response import Response
from .filters import CarFilter
from django_filters import rest_framework as filters
from django.db.models import Sum

class CarView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarGetView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get(self, request, *args, **kwargs):
        data = CarSerializer(Car.objects.all(), many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class CarAggregationView(generics.ListAPIView):
    serializer_class = CarAggregationSerializer
    queryset = Car.objects.all()
