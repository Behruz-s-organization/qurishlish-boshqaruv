# django
from django.contrib import admin


# customers
from core.apps.customers.models import Domain


class DomainInline(admin.TabularInline):
    model = Domain
    extra = 0


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    pass