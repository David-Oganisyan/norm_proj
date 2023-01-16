from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "display_name", "is_active")
    list_display_links = ("username", "email")
    # fields = (
    #     None, {"fields": ("username", "email", "phone", "password")}),
    # (_("Personal_info"), {"fields": ("display_name", "gender", "about", "birthday", "avatar")}),
    # (_("permissions"), {"fields": ("is_staff", "is_active")}),

    search_fields = ("username", "display_name")
    ordering = ("-date_joined",)

#
# admin.site.unregister(User)
# admin.site.register(User)