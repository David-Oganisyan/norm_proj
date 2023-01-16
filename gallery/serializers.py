from rest_framework import serializers
from .models import Publication, Comment
from utils.serializers import RecursiveSerializers, FilterCommentListSerializers
from like import services as like_service


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("publication",
                  "text",
                  "parentt",)


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    children = RecursiveSerializers(many=True)
    user = serializers.ReadOnlyField(source="user.username")

    def get_text(self, obj):
        if obj.is_deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializers
        model = Comment
        fields = ("id",
                  "publication",
                  "user",
                  "text",
                  "created_at",
                  "update_at",
                  "children",)


class PublicationListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    is_fun = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = ("id",
                  "user",
                  "image",
                  "created_at",
                  "is_fun",
                  "likes_count",
                  "comments_count",)


class PublicationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    is_fun = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = ("id",
                  "user",
                  "image",
                  "description",
                  "created_at",
                  "is_fun",
                  "likes_count",
                  "comments",)

    def get_is_fun(self, obj) -> bool:
        user = self.context.get("request").user
        return like_service.is_fun(obj, user)