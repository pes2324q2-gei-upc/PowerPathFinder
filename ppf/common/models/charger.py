"""
Here is the common models for all the applications.

This will be shared through all the dockers and can be accesses by importing it.
"""
from django.db import models
from requests import delete


class LocationCharger(models.Model):
    """
    Model for storing the location of the chargers.
    """
    # class TypeOfCurrent(models.TextChoices):
    #     AC = "AC"
    #     DC = "DC"
    #     AC_DC = "AC/DC"

    # General info
    promotorGestor = models.CharField(max_length=100)
    access = models.CharField(max_length=100)

    # Charger type info
    connectionType = models.ManyToManyField(
        'ChargerLocationType', related_name='connectionType')
    kw = models.FloatField()
    acDc = models.CharField(max_length=5)
    velocities = models.ManyToManyField(
        'ChargerVelocity', related_name='velocities')

    # Location
    latitud = models.FloatField()
    longitud = models.FloatField()
    adreA = models.CharField(max_length=100)

    class Meta:
        app_label = "common"


class ChargerVelocity(models.Model):

    NORMAL = 'NORMAL'
    semiRAPID = 'semiRAPID'
    RAPID = 'RAPID'
    superRAPID = 'superRAPID'

    VELOCITY_CHOICES = [
        (NORMAL, 'NORMAL'),
        (semiRAPID, 'semiRAPID'),
        (RAPID, 'RAPID'),
        (superRAPID, 'superRAPID')
    ]
    velocity = models.CharField(
        max_length=10, choices=VELOCITY_CHOICES, unique=True)

    class Meta:
        app_label = "common"

    def str(self):
        return self.velocity


class ChargerLocationType(models.Model):
    """
    Model to represent the types of chargers.
    """

    MENNEKES = "MENNEKES"
    TESLA = "Tesla"
    SCHUKO = "Schuko"
    CHADEMO = "ChadeMO"
    CCS_COMBO2 = "CCS Combo2"

    CHARGER_CHOICES = [
        (MENNEKES, "MENNEKES"),
        (TESLA, "Tesla"),
        (SCHUKO, "Schuko"),
        (CHADEMO, "ChadeMO"),
        (CCS_COMBO2, "CCS Combo2"),
    ]

    chargerType = models.CharField(
        max_length=20, choices=CHARGER_CHOICES, unique=True)

    def __str__(self):
        return self.chargerType

    class Meta:
        app_label = "common"
