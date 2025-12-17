# django
from django.contrib import admin


# accounts
from core.apps.accounts.models import PermissionGroup
from core.apps.accounts.admin.inlines import PermissionModulInline


@admin.register(PermissionGroup)
class PermissionGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'is_deleted']
    search_fields = ['name']
    inlines = [PermissionModulInline]