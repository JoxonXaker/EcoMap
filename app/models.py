from django.db import models
from utils import preview
from .helper import *


class OrganizationModel(models.Model):
    name = models.CharField(max_length=250, unique=True, editable=True)
    phone = models.CharField(max_length=202, default='not showed', editable=True)
    email = models.EmailField(max_length=100, null=True, blank=True, editable=True)
    region = models.CharField(max_length=20, choices=REGIONS, null=True, editable=True)
    district = models.CharField(max_length=20, choices=DISTRICTS, null=True, editable=True)
    category = models.IntegerField(choices=CATEGORY, editable=True)
    location = models.CharField(max_length=50, null=True, blank=True, editable=True)
    icon = models.ImageField(upload_to='organ_icons', null=True, blank=True, editable=True)
    tree_count = models.IntegerField(default=0, editable=True)
    land_area = models.CharField(max_length=25, default='not showed', editable=True)

    @property
    def img_preview(self):
        return preview.preview_image(self.icon)

    def __str__(self):
        return self.name


class ResponsiblePersonModel(models.Model):
    full_name = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    icon = models.ImageField(upload_to='person_icons', null=True, blank=True)
    position = models.CharField(max_length=100, null=True)
    organization = models.ForeignKey(to=OrganizationModel, related_name='OrganizationPerson', on_delete=models.CASCADE,
                                     null=True)

    @property
    def img_preview(self):
        return preview.preview_image(self.icon)

    def __str__(self):
        return self.full_name


class TreeInfoModel(models.Model):
    name = models.CharField(max_length=50, default='Ninabargli Archa', null=True)
    type = models.IntegerField(choices=TYPES, default=0, null=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    tall = models.CharField(max_length=20, default='3-4', null=True)
    status = models.IntegerField(choices=STATUS, default=1, null=True)  # Daraxt holati
    irrigation = models.IntegerField(choices=STATUS, default=1, null=True)  # sugorish holati
    organization = models.ForeignKey(to=OrganizationModel, on_delete=models.CASCADE, related_name='OrganizationTree')
    responsible = models.ForeignKey(to=ResponsiblePersonModel, on_delete=models.CASCADE, related_name='ResponsibleTree')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.organization} -> id Tree: {self.pk} -> Responsible: {self.responsible}'
