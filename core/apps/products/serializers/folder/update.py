# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# products
from core.apps.products.models import Folder


class UpdateFolderSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate(self, data):
        if Folder.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError(
                {"field": "name", "message": "Bu nom bilan papka qoshilgan, iltomos boshqa nom kiriting"}        
            )
        return data
    
    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.name = validated_data.get('name', instance.name)
            instance.save()
            return instance