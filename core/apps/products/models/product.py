# django
from django.db import models


# shared
from core.apps.shared.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    code = models.CharField(max_length=200)

    folder = models.ForeignKey('products.Folder', on_delete=models.CASCADE, related_name='products')
    sub_folder = models.ForeignKey(
        'products.SubFolder', on_delete=models.SET_NULL, related_name='products', null=True, blank=True
    )
    type = models.ForeignKey('products.ProductType', on_delete=models.CASCADE, related_name='products')
    unit = models.ForeignKey('products.Unit', on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name