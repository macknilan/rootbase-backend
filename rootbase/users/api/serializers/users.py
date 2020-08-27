""" Users serializers """

# Django
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    User login serializer
    Handle the login request data
    """
    class Meta:
        model = User
        fields = ["username", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
