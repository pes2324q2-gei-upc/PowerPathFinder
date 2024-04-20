from django.db import models

from .user import User
from .route import Route


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    paymentIntentId = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.user.username}'s payment of {self.amount} on {self.date}"
