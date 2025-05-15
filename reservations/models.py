from accounts.models import CustomUser
from django.db import models
from restaurants.models import Restaurant

CHOICES = [
    ('COMPLETED', 'completed'),
    ('ACTIVE', 'active'),
    ('CANCELLED', 'cancelled')
]

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    no_of_guests = models.IntegerField(default=1)
    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=True
    )
    # status = models.CharField(
    #     max_length=100,
    #     default='active'
    # )


class Cancellations(models.Model):
    date = models.DateField()
    time = models.TimeField()
    no_of_guests = models.IntegerField(default=1)
    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    reason = models.CharField(max_length=2000)
