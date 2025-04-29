from accounts.models import CustomUser
from django.db import models
from restaurants.models import Restaurant



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


class Cancellations(models.Model):
    reason = models.CharField(max_length=2000)
    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.DO_NOTHING
    )