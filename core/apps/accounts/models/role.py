# django
from django.db import models

# shared
from core.apps.shared.models import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    comment = models.TextField(null=True, blank=True)

    # relationship  
    permission_groups = models.ManyToManyField('accounts.PermissionGroup', related_name="permission_groups")
    permission_modules = models.ManyToManyField('accounts.PermissionModule', related_name="permission_modules")
    permission_actions = models.ManyToManyField('accounts.PermissionAction', related_name="permission_actions")

    def __str__(self):
        return self.name
    