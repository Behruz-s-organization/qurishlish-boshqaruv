# django
from django.contrib import admin


# products
from core.apps.products.models import Product


admin.site.register(Product)