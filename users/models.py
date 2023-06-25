from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from utils import preview


class UserModel(AbstractUser):
    phone_number = models.CharField(
        _('phone number'),
        unique=False,
        max_length=25,
        help_text=_('Make sure you enter your phone number correctly!'),
        error_messages={
            'unique': '"A user with this phone number already exists."'
        },
        null=True,
        blank=True
    )

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists!")
        },
        null=True,
        blank=True
    )
    first_name = models.CharField(_('first name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, null=True, blank=True)
    email = models.EmailField(
        _('email address'),
        help_text=_('Try to enter your email address correctly!'),
        max_length=30,
        unique=False,
        error_messages={
            'unique': _("A user with that email already exists!")
        },
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='avatar/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'email']

    def img_preview(self):
        return preview.preview_image(self.image)

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        elif self.username:
            return self.username
        elif self.phone_number:
            return self.phone_number
