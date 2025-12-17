# django
from django.contrib import admin


# products
from core.apps.products.models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'is_deleted']
    search_fields = ['name']
    ordering = ['-created_at']
