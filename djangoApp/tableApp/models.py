from django.db import models

class Data(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    distance = models.FloatField()