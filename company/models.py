from django.db import models
from api.models import Car

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    cars = models.ManyToManyField(Car)


class CarBrand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Car Brand'
        verbose_name_plural = 'Car Brands'


class CarModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'
