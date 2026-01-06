from django.db import models

# Create your models here.

class Item(models.Model):
    item_name=models.CharField()
    item_desc=models.CharField()
    item_price=models.FloatField()
    item_quantity=models.IntegerField()