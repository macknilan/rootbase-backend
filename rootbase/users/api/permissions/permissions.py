"""User permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    message = 'You do not have permission to access this resource (ᵟຶ︵ ᵟຶ)'

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj