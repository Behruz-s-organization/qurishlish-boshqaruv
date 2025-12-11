# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import Role


class UpdateRoleSerializer(serializers.Serializer):
    name = serializers.CharField()
    comment = serializers.CharField()

    def validate(self, data):
        if Role.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError({"name": "Role with this name already exists"})
        return data
    
    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.name = validated_data.get('name', instance.name)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.save()
            return instance