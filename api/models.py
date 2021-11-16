from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarPart(models.Model):
    name = models.CharField(max_length=256)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='parts', null=True, blank=False)
    qty = models.IntegerField()

    class Meta:
        verbose_name = 'Car Part'
        verbose_name_plural = 'Car Parts'