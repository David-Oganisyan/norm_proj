from rest_framework import serializers
from utils.tools import delete_old_file
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "phone",
            "avatar",
            "display_name",
            "subscriptions_count",
            "subscribers_count",
            "gender",
            "about",
            "birthday",
        )

    def update(self, instance, validated_data):
        delete_old_file(instance.avatar.path)
        return super().update(instance, validated_data)


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "avatar",
            "display_name",
            # "subscriptions_count",
            # "subscribers_count",
            "gender",
            "about",
            "birthday",
        )


class UserByListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "display_name",
            "avatar",
        )