"""User model."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Utilities
from rootbase.utils.models import ROotbaseModel


class User(ROotbaseModel, AbstractUser):
    """User model.
    
    Extend from Django's Abstract User, change the username field
    to email to make it unique.
    
    The required fields are now username, first_name, last_name
    
    The field phone_number is formatted by means of regular expressions

    The new field is created is_client
    
    The new field is created and by defauld is_verfied is set to 
    false until it is verified by mail
    """

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.')
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=_('Phone number must be entered in the format: +999999999. Up to 15 digits allowed.')
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_public = models.BooleanField(
        default=True, help_text=_('Public profiles show all information about users.')
    )

    is_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_(
            'Determine if an user has a verified account. '
            'Set to true when user verified its email address.'
        ),
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Function is overwritten and return username. Instead of first_name"""
        return self.username


# class User(AbstractUser):
#     """Default user for Rootbase.
#     """

#     #: First and last name do not cover name patterns around the globe
#     name = CharField(_("Name of User"), blank=True, max_length=255)

#     def get_absolute_url(self):
#         """Get url for user's detail view.

#         Returns:
#             str: URL for user detail.

#         """
#         return reverse("users:detail", kwargs={"username": self.username})