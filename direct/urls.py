from django.urls import path
from . import views

urlpatterns = [
    path('all', views.DialogListView.as_view({'get': 'list'})),
    path('send/<int:pk>', views.CreateDialogueView.as_view()),
    path('<int:pk>', views.DialogueView.as_view({'get': 'retrieve'})),
    path('massage/send', views.MassageView.as_view({"post": "create"})),
    path('massage/<int:pk>', views.MassageView.as_view({"get": "retrieve"})),
]







