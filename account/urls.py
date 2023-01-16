from django.urls import path

from account import views


urlpatterns = [
    path("profiles/", views.UserListView.as_view({"get": "list"})),
    path("public/<int:pk>", views.UserPublicView.as_view({"get": "retrieve"})),
]