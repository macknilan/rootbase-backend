""" Users API URL's """

from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# from rootbase.users.api.views import UserViewSet
from rootbase.users.api.views.users import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, basename="users")

app_name = "api"
urlpatterns = router.urls
