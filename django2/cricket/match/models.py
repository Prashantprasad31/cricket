from django.db import models

# Create your models here.
class Match(models.Model):
    name=models.CharField(max_length=20)
    score=models.IntegerField()
    strikerate=models.IntegerField()
    


