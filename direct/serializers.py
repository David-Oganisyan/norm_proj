from rest_framework import serializers
from account.serializers import UserByListSerializer
from .models import Dialogue, Massage


class CreateMassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = ("Dialogue",
                  "text")


class MessageSerializer(serializers.ModelSerializer):
    author = UserByListSerializer()
    class Meta:
        model = Massage
        fields = (
            "id",
            "author",
            "text",
            "created_at",
            "dialogue")


class DialogueSerializer(serializers.ModelSerializer):
    auth_user = UserByListSerializer(read_only=True)
    companion = UserByListSerializer(read_only=True)
    massages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Dialogue
        fields = ("id",
                  "companion",
                  "massages",
                  "auth_user",)


class DialogueListSerializer(serializers.ModelSerializer):
    last_massage = serializers.SerializerMethodField()
    class Meta:
        model = Dialogue
        fields = ("author_user",
                  "companion",
                  "last_massage",)

    def get_last_massage(self, obj: Dialogue):
        return MessageSerializer(obj.massage.order_by("created_at").last()).data