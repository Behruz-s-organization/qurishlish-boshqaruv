from django.db import models

from django_tenants.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    auto_create_schema = True