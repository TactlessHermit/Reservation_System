from django.contrib.auth.models import User
from django.db import models
from restaurants.models import Restaurant



class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=True
    )