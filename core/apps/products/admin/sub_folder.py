# django
from django.contrib import admin


# products
from core.apps.products.models import SubFolder


@admin.register(SubFolder)
class SubFolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'folder' 'created_at', 'is_deleted']
    search_fields = ['name', 'folder__name']
    ordering = ['-created_at']