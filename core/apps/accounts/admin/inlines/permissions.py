# django
from django.contrib import admin


# accounts
from core.apps.accounts.models import PermissionAction, PermissionModul


class PermissionActionInline(admin.TabularInline):
    model = PermissionAction
    exta = 0


class PermissionModulInline(admin.TabularInline):
    model = PermissionModul
    extra = 0
