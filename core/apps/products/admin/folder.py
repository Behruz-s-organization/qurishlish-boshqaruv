# django
from django.contrib import admin


# products
from core.apps.products.models import Folder
from core.apps.products.admin.inlines.sub_folder import SubFolderInline


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'is_deleted']
    search_fields = ['name',]
    ordering = ['-created_at']
    inlines = [SubFolderInline]