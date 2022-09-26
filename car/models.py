from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    capacity = models.IntegerField()
    luggage = models.IntegerField()
    air_conditioning = models.BooleanField()
    transmission = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


