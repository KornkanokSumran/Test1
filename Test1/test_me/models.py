from django.db import models

# Create your models here.
class Number(models.Model):
    num = models.IntegerField(default=200)
    count = models.IntegerField(default=1)

