# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# products
from core.apps.products.models import Folder


class CreateFolderSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, value):
        if Folder.objects.filter(name=value).first():
            raise serializers.ValidationError(
                {"field": "name", "message": "Bu nom bilan fayl allaqachon qo'shilgan"}
            )
        return value
    
    def create(self, validated_data):
        with transaction.atomic():
            return Folder.objects.create(
                name=validated_data.get('name')
            )