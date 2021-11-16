from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CarSerializer
from .models import Car
from rest_framework.response import Response


class CarView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
