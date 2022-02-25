from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0)
    stockpile = models.IntegerField(default=0)

    def __str__(self):
        return self.name
