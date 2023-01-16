from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "is_published", "created_at")


class CommentAdmin(MPTTModelAdmin):
    list_display = ("id", "user", "publication", "created_at", "updated_at", "is_published")
    mptt_level_indent = 10


# admin.site.unregister(Publication)
# admin.site.register(Publication)
# admin.site.unregister(MPTTModelAdmin)
# admin.site.register(MPTTModelAdmin)