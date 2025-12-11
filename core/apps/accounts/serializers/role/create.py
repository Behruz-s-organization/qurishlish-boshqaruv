# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import Role


class CreateRoleSerializer(serializers.Serializer):
    name = serializers.CharField()
    comment = serializers.CharField(required=False)

    def validate(self, data):
        if Role.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError({"name": "Role with this name already exists"})
        return data
    
    def create(self, validated_data):
        with transaction.atomic():
            return Role.objects.create(
                name=validated_data.get('name'),
                comment=validated_data.get('comment'),
            )