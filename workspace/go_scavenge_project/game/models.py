from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    picture = models.ImageField(upload_to='profile_image', blank=True)
    about = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.user.username
    
    

class Stat(models.Model):
    user = models.ForeignKey(User)
    longest_session = models.IntegerField()
    max_survivors = models.IntegerField()
    supplies = models.IntegerField()
    
    def __unicode__(self):
        return self.user.username
