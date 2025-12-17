# django
from django.db import models


# shared
from core.apps.shared.models import BaseModel


class SubFolder(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    
    folder = models.ForeignKey('products.Folder', on_delete=models.CASCADE, related_name='sub_folders')

    def __str__(self):
        return f'{self.folder.name} - {self.name}'
    
    @property
    def count_products(self):
        return self.products.count()