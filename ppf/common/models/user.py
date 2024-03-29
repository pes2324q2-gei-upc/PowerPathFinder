"""
Here is the common models for all the applications.

This will be shared through all the dockers and can be accesses by importing it.

__example: from common.models import User, Driver
"""

from django.contrib.auth.models import User as baseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(baseUser):
    """
    User class for our project

    Args:
        baseUser (User): default django implementation for user
            (see the documentation for more info)
    """

    # change to keep the pk defined in the UML consistent
    baseUser.email = models.EmailField("email address", unique=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(
        "Last modification of the User", auto_now=True, auto_now_add=False
    )
    created_at = models.DateTimeField(
        "Creation date of the User", auto_now=False, auto_now_add=True
    )

    # profile_image = models.ImageField(
    #   upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        """
        Meta used to add the label so that the imports work correctly
        """

        app_label = "common"


class Driver(User):
    """
    This is the driver class
    """

    # Pointer to the parent class witch we need since if not done
    # it will end up referencing to baseUser and it will give conflicts.
    # Also note that this will use the default UserManager thus the
    # calls in the serializer create function and the default ones, will reference the
    # UserManager functions such as Driver.objects.create_user instead of
    # Driver.objects.create_driver.
    # If more precise creation is needed the DriverManager class should be implemented
    parent_pointer = models.OneToOneField(
        "User", verbose_name="Parent Class", on_delete=models.CASCADE, parent_link=True
    )

    # Rest of the fields needed
    dni = models.CharField(max_length=50, unique=True)
    driver_points = models.IntegerField(default=0)
    autonomy = models.IntegerField(default=0)

    class Meta:
        """
        Meta used to add the label so that the imports work correctly
        """

        app_label = "common"


class Valuation(models.Model):
    """
    Model for storing valuations given by users to users or drivers.
    """

    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    giver = models.ForeignKey(User, related_name="given_valuations", on_delete=models.CASCADE)
    receiver_user = models.ForeignKey(
        User,
        related_name="received_user_valuations",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)

    class Meta:
        """
        Meta used to add the label so that the imports work correctly
        """

        app_label = "common"
