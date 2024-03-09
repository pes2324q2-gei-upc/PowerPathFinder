"""
    This is the file containing all the classes and models we are gonna use
"""

from django.contrib.auth.models import User as baseUser
from django.db import models


class User(baseUser):
    """
    User class for our project

    Args:
        baseUser (User): default django implementation for user 
            (see the documentation for more info)
    """
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    points = models.IntegerField()
    # profile_image = models.ImageField(
    #   upload_to=None, height_field=None, width_field=None, max_length=None)


class Driver(User):

    """
    This is the driver class
    """
    dni = models.CharField(max_length=50)
    driver_points = models.IntegerField()
