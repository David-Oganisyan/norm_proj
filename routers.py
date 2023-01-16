from django.urls import path, include
from rest_framework import permissions


urlpatterns = [
    path('account', include('account.urls')),
    path('gallery/', include('gallery.urls')),
    path('followers/', include('follower.urls')),
    path('', include('feed.urls')),
    path('direct/', include('direct.urls')),
]