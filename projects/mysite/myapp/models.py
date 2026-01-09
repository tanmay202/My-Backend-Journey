from django.db import models

# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=100) #max length must be declared otherwise it will give error
    item_desc=models.CharField(max_length=200)
    item_price=models.FloatField()
    item_quantity=models.IntegerField()

    def __str__(self):
        return self.item_name #used to display the name on the page otherwise it will display only item object(1),item object(2) etc....

