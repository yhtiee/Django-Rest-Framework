from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, null=False)
    price = models.DecimalField(max_digits=256, decimal_places=2, null=False)