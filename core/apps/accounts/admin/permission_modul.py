# django
from django.contrib import admin


# accounts
from core.apps.accounts.models import PermissionModule
from core.apps.accounts.admin.inlines import PermissionActionInline 


@admin.register(PermissionModule)
class PermissionModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group', 'created_at', 'is_deleted']
    search_fields = ['name', 'group__name']
    inlines = [PermissionActionInline]
