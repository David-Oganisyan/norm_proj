from django.shortcuts import render
from rest_framework import permissions, parsers, response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from account.models import User
from .serializers import CreateMassageSerializer, MessageSerializer, DialogueListSerializer, DialogueSerializer
from .models import Massage, Dialogue
from django.db.models import Q


class DialogListView(ModelViewSet):
    serializer_class = DialogueListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dialogue.objects.filter(Q(auth_user=self.request.user) | Q(companion=self.request.user))


class DialogueView(ModelViewSet):
    serializer_class = DialogueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dialogue.objects.filter(Q(auth_user=self.request.user) | Q(companion=self.request.user))


class CreateDialogueView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except Dialogue.DoesNotExist:
            return response.Response(status=404)
        Dialogue.objects.create(auth_user=request.user, companion=user)
        print("Success")
        return response.Response(status=201)


class MassageView(ModelViewSet):
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = CreateMassageSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Massage.objects.all().select_related("dialog")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
