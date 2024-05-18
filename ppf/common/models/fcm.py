from django.db import models


class FCMToken(models.Model):
    """
    Model to represent the FCM token.
    """

    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="fcm_token")
    token = models.CharField(unique=True)
    ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    def renew(self, token):
        self.token = token
        self.ts
        self.save()

    class Meta:
        app_label = "common"
