from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CarSerializer
from .models import Car


class CarView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
