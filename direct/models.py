from django.db import models
from django.conf import settings


class Dialogue(models.Model):
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name="auth_user")

    companion = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name="companion")

    def __str__(self):
        return f"Dialogue {self.auth_user.username} with {self.companion.username}"

    class Meta:
        verbose_name = "Dialogue"
        verbose_name_plural = "Dialogues"


class Massage(models.Model):
    dialogue = models.ForeignKey(Dialogue,
                                 on_delete=models.CASCADE,
                                 related_name="massage")

    text = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="massage")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Massage from {self.author.username}"


    class Meta:
        verbose_name = "Massage"
        verbose_name_plural = "Massages"
        ordering = ["-created_at"]