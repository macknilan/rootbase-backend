from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from rootbase.users.forms import UserChangeForm, UserCreationForm

# Models
from rootbase.users.models import User, Profile

User = get_user_model()


class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    fieldsets = (("User", {"fields": ("is_verified", "is_public")}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "email", "first_name", "last_name", "is_superuser", "is_verified", "is_public"]
    search_fields = ["username", "email"]


@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    """Profile model admin"""

    list_display = ('user', 'biography', 'picture')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    # list_filter = ('reputation',)


admin.site.register(User, UserAdmin)