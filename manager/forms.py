from django.forms import ModelForm

from .models import OrganizationPhotosModel, PersonPhotosModel, TreePhotosModel


class OrganizationPhotosModelForm(ModelForm):
    class Meta:
        model = OrganizationPhotosModel
        fields = ['icon', 'tag']


class PersonPhotosModelForm(ModelForm):
    class Meta:
        model = PersonPhotosModel
        fields = ['icon', 'tag']


class TreePhotosModelForm(ModelForm):
    class Meta:
        model = TreePhotosModel
        fields = ['icon', 'tag']
