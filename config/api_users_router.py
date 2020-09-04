""" Users API URL's """

# Django
from django.conf import settings

# Django REST Framework
from rest_framework.routers import DefaultRouter, SimpleRouter

# Views
from rootbase.users.api.views.users import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, basename="users")

app_name = "api"
urlpatterns = router.urls
