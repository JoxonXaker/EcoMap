from django.db import models
from utils import crop, preview


class PersonPhotosModel(models.Model):
    photo = models.ImageField(upload_to='person_photos/', null=True, blank=True)
    person = models.ForeignKey(to='app.ResponsiblePersonModel', on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=20, null=True, blank=True)

    def img_preview(self):
        return preview.preview_image(self.photo)

    def __str__(self):
        return self.person.full_name


class OrganizationPhotosModel(models.Model):
    photo = models.ImageField(upload_to='organ_photos/', null=True, blank=True)
    organ = models.ForeignKey(to='app.OrganizationModel', related_name='OrganizationPhotos', on_delete=models.CASCADE,
                              null=True)
    tag = models.CharField(max_length=20, null=True, blank=True)

    def img_preview(self):  # image preview for admin panel
        return preview.preview_image(self.photo)

    def __str__(self):
        return self.organ.name


class TreePhotosModel(models.Model):
    photo = models.ImageField(upload_to='tree_photos/', null=True, blank=True)
    tree = models.ForeignKey(to='app.TreeInfoModel', related_name='TreeInfoPhotos', on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=20, null=True, blank=True)

    def img_preview(self):
        return preview.preview_image(self.photo)

    def __str__(self):
        return self.tree.name
