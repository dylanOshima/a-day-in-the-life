from django.db import models

class Video(models.Model):
    title= models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
class Channel(models.Model):
    name=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    



