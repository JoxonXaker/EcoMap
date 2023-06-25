from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserModel


# For Admins
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'email']


# For Admins
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('phone_number', 'email', 'username', 'first_name', 'last_name', 'image')
