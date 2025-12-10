# django
from django.contrib import admin

# accounts
from core.apps.accounts.models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']