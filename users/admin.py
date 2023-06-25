from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['img_preview', 'username', 'phone_number', 'email']
    list_display_links = ['img_preview', 'username', 'phone_number', 'email']
    readonly_fields = ['img_preview']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (gettext_lazy('Communication'), {'fields': ('phone_number', 'email')}),
        (gettext_lazy('Personal info'), {'fields': ('first_name', 'last_name', 'image')}),
        (gettext_lazy('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'username', 'password1', 'password2'),
        }),
    )
