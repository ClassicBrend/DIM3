from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=true)
    password = models.CharField(max_length=30)

class Stats(models.Model):
    user = models.ForeignKey(User)
    longest_session = models.CharField(max_length=30)
    max_survivors = models.CharField(max_length=30)
        


    
    
    
        

