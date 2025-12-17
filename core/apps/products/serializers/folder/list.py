# rest framework
from rest_framework import serializers


# products
from core.apps.products.models import Folder


class ListFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = [
            'id',
            'name',
            'count_products',
            'created_at',
            'updated_at',
        ]