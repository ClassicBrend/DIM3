from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)

class Stat(models.Model):
    user = models.ForeignKey(User)
    longest_session = models.CharField(max_length=30)
    max_survivors = models.CharField(max_length=30)
    supplies = models.IntegerField()
    game_data = models.CharField(max_length=1000)
    
        


    
    
    
        

