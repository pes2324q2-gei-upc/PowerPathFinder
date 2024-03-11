"""
Data models definition for all PowerPathFinder services, this module serves as single source of
truth. Other services will introspect the DB in order to be up to date. It includes the following
models:

- Route: Describes the routes that drivers can create and passenjers can join.
- RoutePassenjers: Describes the passenjers that are part of a route, records are created when
    users join to a route.
"""
from django.db import models
from .user import Driver, User

class Route(models.Model):
    """
    Route between two points, organized by a driver to be shared with passenjers.
    """
    id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    originLatitude = models.FloatField()
    originLongitude = models.PositiveBigIntegerField()
    originAlias = models.CharField(max_length=100)
    destinationLatitude = models.PositiveBigIntegerField()
    destinationLongitude = models.PositiveBigIntegerField()
    destinationAlias = models.CharField(max_length=100)
    departureTime = models.DateTimeField()
    autonomy = models.PositiveBigIntegerField()
    maxAutonomy = models.PositiveBigIntegerField()
    freeSeats = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    class Meta:
        app_label = 'common'

class RoutePassenjer(models.Model):
    """
    Represents the passenjers that are part of a route, records are created when users join to a
    route.
    """
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenjer = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        app_label = 'common'
