"""
Data models definition for all PowerPathFinder services, this module serves as single source of
truth. Other services will introspect the DB in order to be up to date. It includes the following
models:

- Route: Describes the routes that drivers can create and passenjers can join.
- RoutePassenjers: Describes the passenjers that are part of a route, records are created when
    users join to a route.
"""

from django.db import models

class User(models.Model):
    """
    Placeholder
    """
    class Meta:
        app_label = 'common'

class Route(models.Model):
    """
    Represents a route between two points, organized by a driver to be shared with passenjers.
    
    Attributes:
    - id: Route unique identifier.
    - driver: User unique identifier.
    - originLatitude: Origin point latitude.
    - originLongitude: Origin point longitude.
    - originAlias: Origin point name (ie: street name).
    - destinationLatitude: Destination point latitude.
    - destinationLongitude: Destination point longitude.
    - destinationAlias: Destination point name (ie: street name).
    - departureTime: Departure date time.
    - autonomy: Expected vehicle autonomy at departure.
    - maxAutonomy: Vehicle max autonomy.
    - freeSeats: Current available seats at a given moment.
    - price: Total price for the route calculated by... #TODO
    """
    id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
    Attributes:
    - id: Route passenjer unique identifier.
    - route: Route unique identifier.
    - passenjer: User unique identifier.
    - seat: Seat number assigned to the passenjer.
    - price: Price paid by the passenjer for the route.
    """
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenjer = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.PositiveBigIntegerField()
    class Meta:
        app_label = 'common'
