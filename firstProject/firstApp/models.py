from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()