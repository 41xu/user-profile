from django.db import models

# Create your models here.

class appInfo(models.Model):
    appid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    male=models.FloatField()
    female=models.FloatField()
    age_24=models.FloatField()
    age_25_30=models.FloatField()
    age_31_35=models.FloatField()
    age_36_40=models.FloatField()
    age_40=models.FloatField()