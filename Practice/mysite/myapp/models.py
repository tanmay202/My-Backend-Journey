from django.db import models

# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=100)
    item_quantity=models.IntegerField()
    item_desc=models.CharField(max_length=500)
    item_price=models.FloatField()

    def __str__(self):
        return self.item_name