from django.db import models

class Peak(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    altitude = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)
