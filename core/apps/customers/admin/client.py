# django
from django.contrib import admin

# django tenants
from django_tenants.admin import TenantAdminMixin

# curstomers
from core.apps.customers.models import Client
from core.apps.customers.admin.domain import DomainInline


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'schema_name']
    search_fields = ['name']
    inlines = [DomainInline]