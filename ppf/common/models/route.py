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

    originLat = models.FloatField()
    originLon = models.FloatField()
    originAlias = models.CharField(max_length=100)

    destinationLat = models.FloatField()
    destinationLon = models.FloatField()
    destinationAlias = models.CharField(max_length=100)

    polyline = models.TextField()
    distance = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

    departureTime = models.DateTimeField()
    arrivalTime = models.DateTimeField()
    freeSeats = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField(default=0)

    cancelled = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)

    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "common"


class RoutePassenjer(models.Model):
    """
    Represents the passenjers that are part of a route, records are created when users join to a
    route.
    """

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenjer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = "common"
