from django.db import models


class Product(models.Model):
    """
        model for product in db
    """
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stockpile = models.IntegerField(default=0)
    can_be_sold = models.BooleanField(default=True)

    def __str__(self):
        return self.name
