"""
Here is the common models for all the applications.

This will be shared through all the dockers and can be accesses by importing it.

__example: from ppf.common.models import User, Driver
"""

from django.contrib.auth.models import User as baseUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(baseUser):
    """
    User class for our project

    Args:
        baseUser (User): default django implementation for user 
            (see the documentation for more info)
    """
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    points = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(
        "Last modification of the User", auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(
        "Creation date of the User", auto_now=False, auto_now_add=True)

    # profile_image = models.ImageField(
    #   upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        """
            Meta used to add the label so that the imports work correctly
        """
        app_label = 'common'


class Driver(User):
    """
    This is the driver class
    """
    dni = models.CharField(max_length=50)
    driver_points = models.IntegerField()

    class Meta:
        """
            Meta used to add the label so that the imports work correctly
        """
        app_label = 'common'


class Valuation(models.Model):
    """
    Model for storing valuations given by users to users or drivers.
    """
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    giver = models.ForeignKey(
        User, related_name='given_valuations', on_delete=models.CASCADE)
    receiver_user = models.ForeignKey(
        User, related_name='received_user_valuations',
        on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[
                                 MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)

    class Meta:
        """
            Meta used to add the label so that the imports work correctly
        """
        app_label = 'common'
