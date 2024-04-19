"""
Here is the common models for all the applications.

This will be shared through all the dockers and can be accesses by importing it.

__example: from common.models import User, Driver
"""

from django.contrib.auth.models import User as baseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .route import Route


class User(baseUser):
    """
    User class for our project

    Args:
        baseUser (User): default django implementation for user
            (see the documentation for more info)
    """

    # change to keep the pk defined in the UML consistent
    baseUser.email = models.EmailField("email address", unique=True)  # type: ignore
    birthDate = models.DateField(auto_now=False, auto_now_add=False)
    points = models.IntegerField(default=0)
    updatedAt = models.DateTimeField(
        "Last modification of the User", auto_now=True, auto_now_add=False
    )
    createdAt = models.DateTimeField("Creation date of the User", auto_now=False, auto_now_add=True)

    # profile_image = models.ImageField(
    #   upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        """
        Meta used to add the label so that the imports work correctly
        """

        app_label = "common"


class ChargerType(models.Model):
    """
    Model to represent the types of chargers.
    """

    MENNEKES = "Mennekes"
    TESLA = "Tesla"
    SCHUKO = "Schuko"
    CHADEMO = "ChadeMO"
    CSS_COMBO2 = "CSS Combo2"

    CHARGER_CHOICES = [
        (MENNEKES, "Mennekes"),
        (TESLA, "Tesla"),
        (SCHUKO, "Schuko"),
        (CHADEMO, "ChadeMO"),
        (CSS_COMBO2, "CSS Combo2"),
    ]

    chargerType = models.CharField(max_length=20, choices=CHARGER_CHOICES, unique=True)

    def __str__(self):
        return self.chargerType


class Preference(models.Model):
    """
    Model to represent driver preferences.
    """

    canNotTravelWithPets = models.BooleanField(default=False)
    listenToMusic = models.BooleanField(default=False)
    noSmoking = models.BooleanField(default=False)
    talkTooMuch = models.BooleanField(default=False)

    def __str__(self):
        return (
            "Travel Preferences: Can't Travel With Pets - "
            + str(self.canNotTravelWithPets)
            + ", Listen to Music - "
            + str(self.listenToMusic)
            + ", No Smoking - "
            + str(self.noSmoking)
            + ", Talk Too Much - "
            + str(self.talkTooMuch)
        )


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
    driverPoints = models.IntegerField(default=0)
    autonomy = models.IntegerField(default=0)

    # Charger type attributes
    chargerTypes = models.ManyToManyField("ChargerType", related_name="drivers")

    # Preferences attributes
    preference = models.OneToOneField("Preference", on_delete=models.CASCADE, null=True)

    iban = models.CharField(max_length=36, unique=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        """
        Override of the save method to add the preference if it does not exist
        """
        if not hasattr(self, "iban") or self.iban == "":
            # Cannot exist without an iban
            raise ValueError("Iban is required for a driver")
        if not hasattr(self, "preference") or not self.preference:
            self.preference = Preference.objects.create()

        return super().save(*args, **kwargs)

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
    receiver = models.ForeignKey(
        User,
        related_name="received_user_valuations",
        on_delete=models.CASCADE,
    )
    route = models.ForeignKey(Route, related_name="route_valuations", on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)

    class Meta:
        """
        Meta used to add the label so that the imports work correctly
        """

        app_label = "common"
        unique_together = ("giver", "receiver", "route")


class Report(models.Model):
    """
    Model for storing Reports given by users to users or drivers.
    """

    reporter = models.ForeignKey(User, related_name="report_giver", on_delete=models.CASCADE)
    reported = models.ForeignKey(User, related_name="report_receiver", on_delete=models.CASCADE)

    updatedAt = models.DateTimeField(
        "Last modification of the Report", auto_now=True, auto_now_add=False
    )
    createdAt = models.DateTimeField(
        "Creation date of the Report", auto_now=False, auto_now_add=True
    )

    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.reporter} -> {self.reported}"

    class Meta:
        """
        Meta used to add the label so that the imports work correctly
        """

        app_label = "common"
