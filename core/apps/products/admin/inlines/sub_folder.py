# django
from django.contrib import admin


# products
from core.apps.products.models import SubFolder


class SubFolderInline(admin.TabularInline):
    model = SubFolder
    extra = 0