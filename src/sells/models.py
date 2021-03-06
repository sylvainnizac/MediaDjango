from datetime import datetime

from django.db import models
from src.products.models import Product

class Sell(models.Model):
    """
        model for sell in db
    """
    client_name = models.CharField(max_length=128)
    date = models.DateField(default=datetime.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.0)
