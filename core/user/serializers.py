from rest_framework import serializers
from django.conf import settings

from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "username",
            "name",
            "first_name",
            "last_name",
            "bio",
            "email",
            "is_active",
            "created",
            "updated",
        ]
        # List of all the fields that can only be read by the user
        read_only_field = ["is_active"]
