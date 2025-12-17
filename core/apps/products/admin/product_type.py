# django
from django.contrib import admin


# products
from core.apps.products.models import ProductType


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'is_deleted']
    search_fields = ['name']
    ordering = ['-created_at']