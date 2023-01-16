from rest_framework import serializers
from account.serializers import UserByListSerializer
from .models import Follower


class FollowerListSerializer(serializers.ModelSerializer):
    subscriber = UserByListSerializer()
    model = Follower
    fields = ("subscriber",)