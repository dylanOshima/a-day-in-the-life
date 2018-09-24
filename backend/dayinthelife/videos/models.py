from django.db import models

class Video(models.Model):
    title= models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=500)
    code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Page(models.Model):
    number=models.CharField(max_length=500)
    
    def __str__(self):
        return self.number
    



