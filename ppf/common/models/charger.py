"""
Here is the common models for all the applications.

This will be shared through all the dockers and can be accesses by importing it.
"""
from django.db import models
from models.user import ChargerType


class LocationCharger(models.Model):
    """
    Model for storing the location of the chargers.
    """
    class TypeOfCurrent(models.TextChoices):
        AC = "AC"
        DC = "DC"
        AC_DC = "AC/DC"

    # General info
    promotorGestor = models.CharField(max_length=100)
    access = models.CharField(max_length=100)

    # Charger type info
    connectionType = models.ManyToManyField(
        ChargerType, related_name='connectionType')
    kw = models.FloatField()
    acDc = models.CharField(choices=TypeOfCurrent.choices, max_length=5)
    velocities = models.ManyToManyField(
        'ChargerVelocity', related_name='velocities')

    # Location
    latitud = models.FloatField()
    longitud = models.FloatField()
    adreA = models.CharField(max_length=100)

    class Meta:
        app_label = "common"


class ChargerVelocity(models.Model):
    VELOCITY_CHOICES = [
        ('NORMAL', 'NORMAL'),
        ('semiRAPID', 'superRAPID'),
        ('RAPID', 'RAPID'),
        ('superRAPID', 'superRAPID')
    ]
    velocity = models.CharField(
        max_length=10, choices=VELOCITY_CHOICES, default='NORMAL')

    class Meta:
        app_label = "common"

    def str(self):
        return self.velocity
