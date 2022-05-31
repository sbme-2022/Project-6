from django.db import models

# Create your models here.
class currencies(models.Model):
    fromCurrency = models.CharField(max_length=10)
    toCurrency = models.CharField(max_length=10)
    rate = models.FloatField()