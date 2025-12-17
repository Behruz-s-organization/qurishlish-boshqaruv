# djano
from django.db import models


# shared
from core.apps.shared.models import BaseModel


class PermissionModul(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    
    group = models.ForeignKey('accounts.PermissionGroup', on_delete=models.CASCADE, related_name='permission_modules')

    def __str__(self):
        return f'{self.group.name} - {self.name}'