from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)


class dish(models.Model):
    Restaurant = models.ManyToManyField(Restaurant)
    name = models.CharField(max_length=500)

    def __str__(self):
        return "%s the restaurant" % self.dish.name
