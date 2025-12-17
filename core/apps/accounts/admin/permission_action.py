# django
from django.contrib import admin


# accounts
from core.apps.accounts.models import PermissionAction


@admin.register(PermissionAction)
class PermissionActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'module', 'created_at', 'is_deleted']
    search_fields = ['name', 'module__name']

