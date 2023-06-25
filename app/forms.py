from django import forms
from .models import OrganizationModel


class OrganizationModelAdminForm(forms.ModelForm):
    class Meta:
        model = OrganizationModel
        fields = ['region', 'district', 'category', 'name', 'phone', 'email', 'location', 'icon', 'tree_count',
                  'land_area']

