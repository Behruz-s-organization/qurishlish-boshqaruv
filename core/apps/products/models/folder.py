# django
from django.db import models


# shared
from core.apps.shared.models import BaseModel


class Folder(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name

    @property
    def count_products(self):
        return self.products.count()