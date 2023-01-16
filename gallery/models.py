from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from mptt.fields import TreeForeignKey
from utils.tools import get_path_upload_image
from mptt.models import MPTTModel
from like.models import Like


class Publication(models.Model):
    image = models.FileField("Publication",
                             upload_to=get_path_upload_image,
                             validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "mov", "mp4"])],)

    description = models.CharField("Description", max_length=500, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    is_published = models.BooleanField("Published", default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Images")
    like = GenericRelation(Like)

    def __str__(self):
        return f"{self.id} from {self.user}"

    @property
    def likes_count(self):
        return self.like.count()

    def comments_count(self):
        return self.comments.count()

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publication"
        # ordering = ["-crated_at"]


class Comment(MPTTModel):
    text = models.TextField("Text", max_length=500)
    created_at = models.DateTimeField("Added", auto_now_add=True)
    updated_at = models.DateTimeField("Changed", auto_now=True)
    is_published = models.BooleanField("Published", default=True)
    is_deleted = models.BooleanField("Deleted", default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name="Comments", on_delete=models.CASCADE)
    parent = TreeForeignKey("self",
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name="children")

    def __str__(self):
        return "{} - {}".format(self.user, self.publication)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        # ordering = ["-created_at"]