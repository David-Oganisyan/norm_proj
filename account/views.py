from rest_framework import permissions, filters, parsers
from rest_framework.viewsets import ModelViewSet
from utils.tools import delete_old_file
from .models import User
from .serializers import (
    UserSerializers,
    UserPublicSerializer,
    UserByListSerializer,
)


class UserListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserByListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "display_name"]


class UserView(ModelViewSet):
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def perform_destroy(self, instance):
        delete_old_file(instance.avatar.path)
        instance.delete()


class UserPublicView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.AllowAny]



