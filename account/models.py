from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
from utils.tools import get_path_upload_avatar, validate_size_image
from .managers import UserManager


class User(AbstractUser):
    GENDER = {
        ("M", "Male"),
        ("F", "Female"),
        ("P", "Prefer not to mention"),
    }

    username = models.CharField("Login", max_length=50, unique=True)
    email = models.EmailField("Email", unique=True)
    display_name = models.CharField("Name", max_length=50, blank=True, null=True)
    phone = models.CharField("Phone", max_length=50, unique=True, blank=True, null=True)
    gender = models.CharField("Gender", max_length=1, choices=GENDER, default="P")
    about = models.TextField("About me", max_length=255, blank=True, null=True)
    birthday = models.DateTimeField("Birthday", blank=True, null=True)
    avatar = models.ImageField(
        "Avatar",
        upload_to=get_path_upload_avatar,
        validators=[FileExtensionValidator(allowed_extensions=["jpg"]), validate_size_image],
        default=settings.DEFAULT_AVATAR,
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.username

    # def subscriptions_count(self):
    #     return self.subscriber.count()
    #
    # def subscribers_count(self):
    #     return self.subscribers.count()

    class Meta:

        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]

