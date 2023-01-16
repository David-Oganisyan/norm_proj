"""ByteCord URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    # path('', include('account.urls')),
    path('admin/', admin.site.urls),
    path("api/auth", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("", include("routers")),
    # path('', include('direct.urls')),
    # path("", include("gallery.urls")),
    # path("user/", UserListView.as_view({"get": "list"})),
    path("api/vi/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/vi/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/vi/token/verify", TokenVerifyView.as_view(), name="token_verify"),
    # path(r'^auth/', include('djoser.urls')),
    # path('api/v1/auth/', include('djoser.urls')), # получает список всех пользователей
]

