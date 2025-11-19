from django.contrib import admin

from core.apps.customers.models import Client
from core.apps.customers.admin.domain import DomainInline


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'schema_name']
    search_fields = ['name']
    inlines = [DomainInline]