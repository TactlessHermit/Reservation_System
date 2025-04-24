from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)
    no_of_tables = models.IntegerField()