from django.db import models
from company.models import  CarModel

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars', null=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarPart(models.Model):
    name = models.CharField(max_length=256)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='parts', null=True, blank=False)
    qty = models.IntegerField()
    replacable = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = 'Car Part'
        verbose_name_plural = 'Car Parts'


class CarBrokenPart(models.Model):
    name = models.CharField(max_length=256)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='broken_parts', null=True, blank=False)
    qty = models.IntegerField()
    repairable = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = 'Car Broken Part'
        verbose_name_plural = 'Car Broken Part'


class Bike(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    class Meta:
        verbose_name = 'Bike'
        verbose_name_plural = 'Bike'