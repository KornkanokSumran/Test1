from django.db import models

# Create your models here.
class num(models.Model):
    Number = models.IntegerField(max_length=200)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.Number