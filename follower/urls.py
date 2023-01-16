from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.FollowerListView.as_view({"get": "list"})),
    path("user/<int:pk>/", views.FollowerView.as_view()),
]