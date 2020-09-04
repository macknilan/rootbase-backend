""" Users Views """

# Django
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
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
# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rootbase.users.api.permissions import IsAccountOwner

# Models
from rootbase.users.models.users import User

# User = get_user_model()

class UserViewSet(mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """
    # Make query of active users
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    # Instead of doing the search by the ID/PK,
    # the search is made by the username in the URL
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action.
        
        If the action is retrieve, custom permission is added
        so that only the same User can be edited and viewed
        """
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action == 'retrieve':
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

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

    # def retrieve(self, request, *args, **kwargs):
    #     """Add extra data to the response.
    #     
    #     Retrive/list data of the current user
    #     """
    #     response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
    #     circles = Circle.objects.filter(
    #         members=request.user,
    #         membership__is_active=True
    #     )
    #     data = {
    #         'user': response.data,
    #         'circles': CircleModelSerializer(circles, many=True).data
    #     }
    #     response.data = data
    #     return response