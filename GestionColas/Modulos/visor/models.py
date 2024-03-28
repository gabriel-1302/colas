from django.db import models

# Create your models here.
class Ficha(models.Model):
    numero=models.CharField(max_length = 10)
    doctor=models.CharField(max_length = 10,blank=True)
    