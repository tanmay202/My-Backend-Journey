from django.db import models

# Create your models here.
class Myclass(models.Model):
    game_Name=models.CharField(max_length=200)
    game_rating=models.IntegerField()
    game_details=models.CharField()