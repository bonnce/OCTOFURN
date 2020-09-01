from django.db import models

# Create your models here.
class Clientes(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    direction=models.CharField(max_length=60)