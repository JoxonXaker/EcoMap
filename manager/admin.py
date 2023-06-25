from django.contrib import admin

from .models import OrganizationPhotosModel, PersonPhotosModel, TreePhotosModel


class OrganizationPhotosModelTabularInline(admin.TabularInline):
    model = OrganizationPhotosModel
    readonly_fields = ['img_preview']
    extra = 5
    min_num = 2
    max_num = 5


class PersonPhotosModelTabularInline(admin.TabularInline):
    model = PersonPhotosModel
    readonly_fields = ['img_preview']
    extra = 5
    min_num = 2
    max_num = 5


class TreePhotosModelTabularInline(admin.TabularInline):
    model = TreePhotosModel
    readonly_fields = ['img_preview']
    extra = 5
    min_num = 2
    max_num = 5


@admin.register(OrganizationPhotosModel)
class OrganizationPhotosModelAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['img_preview', '__str__']
    list_display_links = ['img_preview', '__str__']


@admin.register(PersonPhotosModel)
class PersonPhotosModelAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['img_preview', '__str__']
    list_display_links = ['img_preview', '__str__']


@admin.register(TreePhotosModel)
class TreePhotosModelAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['img_preview', '__str__']
    list_display_links = ['img_preview', '__str__']
