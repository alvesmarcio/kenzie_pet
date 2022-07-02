from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)
    
    characteristic = models.ManyToManyField(to='characteristics.Characteristic')