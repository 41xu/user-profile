from django.db import models

# Create your models here.

class User(models.Model):
    id=models.IntegerField(primary_key=True,default=0)
    tel=models.IntegerField()
    appid=models.IntegerField()
    time=models.IntegerField()
    count=models.IntegerField()

