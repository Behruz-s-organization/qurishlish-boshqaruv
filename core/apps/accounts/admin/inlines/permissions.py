# django
from django.contrib import admin


# accounts
from core.apps.accounts.models import PermissionAction, PermissionModule


class PermissionActionInline(admin.TabularInline):
    model = PermissionAction
    exta = 0


class PermissionModuleInline(admin.TabularInline):
    model = PermissionModule
    extra = 0
