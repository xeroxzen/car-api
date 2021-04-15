from django.db import models

# Create your models here.

class Car(models.Models):
    name = models.Charfield(max_length=100)
    top_speed = models.IntegerField()