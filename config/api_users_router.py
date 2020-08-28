""" Users API URL's """

# # Django
# from django.conf import settings
# 
# # Django REST Framework
# from rest_framework.routers import DefaultRouter, SimpleRouter
# 
# # from rootbase.users.api.views import UserViewSet
# from rootbase.users.api.views.users import UserViewSet
# 
# if settings.DEBUG:
#     router = DefaultRouter()
# else:
#     router = SimpleRouter()
# 
# # router = DefaultRouter(trailing_slash=False)
# router.register("users", UserViewSet, basename="users")
# 
# app_name = "api"
# urlpatterns = router.urls

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

# Django
from django.conf import settings
from django.urls import path

# Views
from rootbase.users.api.views.users import (
    AccountVerificationAPIView,
    UserLoginAPIView,
    UserSignUpAPIView
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/verify/', AccountVerificationAPIView.as_view(), name='verify'),
]

app_name = "api"
# urlpatterns = router.urls