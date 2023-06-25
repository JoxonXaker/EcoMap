from django.contrib import admin

from manager.admin import TreePhotosModelTabularInline, OrganizationPhotosModelTabularInline, \
    PersonPhotosModelTabularInline
from .models import TreeInfoModel, OrganizationModel, ResponsiblePersonModel
from .forms import OrganizationModelAdminForm


@admin.register(TreeInfoModel)
class TreeInfoModelAdmin(admin.ModelAdmin):
    list_display = ['type', 'status', 'organization', 'responsible', 'location']
    list_display_links = ['type', 'status', 'organization', 'responsible']
    inlines = [TreePhotosModelTabularInline]


class OrganizationTreeModelStackedInline(admin.TabularInline):
    model = TreeInfoModel
    extra = 0


@admin.register(OrganizationModel)
class OrganizationModelAdmin(admin.ModelAdmin):
    form = OrganizationModelAdminForm
    readonly_fields = ['img_preview']
    list_display = ['img_preview', 'name', 'region', 'district']
    list_editable = ['name']
    list_display_links = ['img_preview', 'region', 'district']
    search_fields = ['name', 'region', 'district']
    inlines = [OrganizationPhotosModelTabularInline]

    class Media:
        js = (
            '/static/assets/js/admin.js',
        )


@admin.register(ResponsiblePersonModel)
class ResponsiblePersonModelAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['img_preview', 'full_name', 'organization']
    list_editable = []
    list_display_links = ['full_name', 'organization']
    inlines = [PersonPhotosModelTabularInline]
