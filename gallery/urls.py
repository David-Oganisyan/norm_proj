from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.PublicationListView.as_view({"get": "list"})),
    path("publication", views.PublicationView.as_view({"post": "create"})),
    path("publication/<int:pk>", views.PublicationView.as_view({"get": "retrieve",
                                                                "put": "update",
                                                                "delete": "destroy"})),
    path("publication/<int:pk>/like", views.PublicationView.as_view({"post": "like"})),
    path("publication/<int:pk>/unlike", views.PublicationView.as_view({"post": "unlike"})),
    # path("publication/<int:pk/fans>", views.PublicationView.as_view({"get": "fans"})),
    path("comment", views.CommentView.as_view({"post": "create"})),
    path("comment/<int:pk>", views.CommentView.as_view({"get": "retrieve",
                                                        "put": "update",
                                                        "delete": "destroy"})),
]
