from django.db import models

class UserProfile(models.Model):
    username = models.OneToOneField(blank=full, Primary_Key=True)
    def __unicode__(self):
        return self.username
    
class Game(models.Model):
    gameID = models.IntegerField(Primary_Key=True)
    score = models.IntegerField()

    
class Leaderboard(models.Model):
    name = models.ForeignKey(UserProfile)
    gameID = models.ForeignKey(Game)
    score = models.IntegerField()
    
class Supplies(models.Model):
    supplyName = models.CharField(max_length=60)
    supplyType = models.CharField(max_length=60)
    
    
    
    
        

