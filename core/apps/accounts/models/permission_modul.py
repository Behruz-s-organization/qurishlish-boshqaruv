# djano
from django.db import models


# shared
from core.apps.shared.models import BaseModel


class PermissionModule(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    
    group = models.ForeignKey('accounts.PermissionGroup', on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return f'{self.group.name} - {self.name}'