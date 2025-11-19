from django.contrib import admin

from core.apps.customers.models import Domain


class DomainInline(admin.TabularInline):
    model = Domain
    extra = 0