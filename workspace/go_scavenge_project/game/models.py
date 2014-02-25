from django.db import models

class User(models.Model):
    username = models.OneToOneField(blank=true, Primary_Key=True)
    def __unicode__(self):
        return self.username
        


    
    
    
        

