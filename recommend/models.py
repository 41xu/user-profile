from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    tel = models.IntegerField()
    appid = models.IntegerField()
    time = models.IntegerField()
    count = models.IntegerField()
