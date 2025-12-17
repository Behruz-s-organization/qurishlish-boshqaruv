# djano
from django.db import models


# shared
from core.apps.shared.models import BaseModel


class PermissionAction(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    modul = models.ForeignKey('accounts.PermissionModule', on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return f'{self.modul.name} - {self.name}'