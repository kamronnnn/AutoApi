from django.db import models

# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=50)
    max_speed = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    production_year = models.IntegerField(default=2000)
    marka_car = models.CharField(max_length=50)


    def __str__(self):
        return self.model
