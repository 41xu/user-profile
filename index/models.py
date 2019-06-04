from django.db import models



class Table(models.Model):
    name=models.CharField(max_length=20)