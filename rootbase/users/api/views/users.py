""" Users Views """

# Django
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

# Serializers
# from .serializers import UserSerializer
# from rootbase.users.api.serializers.users import UserSerializer
from rootbase.users.api.serializers.users import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# User = get_user_model()


class UserViewSet(viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """

    @action(detail=False, methods=["POST"])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Pshhhkkkkkkrrrr​kakingkakingkakingtsh​chchchchchchchcch​*ding*ding*ding* Congratulation! u r verified in App-In-Develop'}
        return Response(data, status=status.HTTP_200_OK)
