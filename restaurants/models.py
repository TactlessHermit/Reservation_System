from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)
    no_of_tables = models.IntegerField()

    # STRING REPRESENTATION OF OBJECT (FOR ADMIN)
    def __str__(self):
        return "{} in {}".format(self.name, self.location)


class Tag(models.Model):
    name = models.TextField(max_length=100)

    # STRING REPRESENTATION OF OBJECT (FOR ADMIN)
    def __str__(self):
        return self.name


class RestaurantTags(models.Model):
    pk = models.CompositePrimaryKey("restaurant_id", "tag_id")
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )