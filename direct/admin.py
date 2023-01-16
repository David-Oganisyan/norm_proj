from django.contrib import admin
from .models import Dialogue, Massage

@admin.register(Dialogue)
class DialogueAdmin(admin.ModelAdmin):
    list_display = ("id", "auth_user", "companion")


@admin.register(Massage)
class DialogueAdmin(admin.ModelAdmin):
    list_display = ("id", "dialogue", "text", "author", "created_at")
    search_fields = ("dialogue",)
    ordering = ("-crated_at",)


admin.site.unregister(Dialogue)
admin.site.register(Dialogue)
admin.site.unregister(Massage)
admin.site.register(Massage)

