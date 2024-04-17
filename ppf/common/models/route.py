"""
Data models definition for all PowerPathFinder services, this module serves as single source of
truth. Other services will introspect the DB in order to be up to date. It includes the following
models:

- Route: Describes the routes that drivers can create and passengers can join.
- RoutePassengers: Describes the passengers that are part of a route, records are created when
    users join to a route.
"""

from django.db import models

from .user import Driver, User


class Route(models.Model):
    """
    Route between two points, organized by a driver to be shared with passengers.
    """

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
    freeSeats = models.PositiveSmallIntegerField()
    price = models.FloatField(default=0.0)

    passengers = models.ManyToManyField(User, related_name="joined_routes")

    cancelled = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)

    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "common"

    def isFull(self):
        """
        Returns True if the route is full, False otherwise.
        """
        return self.freeSeats == 0

    def overlapsWith(self, routeId):
        """
        Returns True if the route temporally overlaps with the route with the provided ID, False otherwise.
        """
        route = Route.objects.get(id=routeId)
        if self.departureTime + self.duration >= route.departureTime:
            return True
        return False
