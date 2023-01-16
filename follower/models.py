from django.db import models
from django.conf import settings
# Create your models here.


class Follower(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner")
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriber")

    def __str__(self):
        return f"{self.subscriber.username} followed {self.user.username}"

    class Meta:
        verbose_name = "Followers"
        verbose_name_plural = verbose_name