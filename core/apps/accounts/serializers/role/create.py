# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import Role, PermissionGroup, PermissionModule, PermissionAction


class CreateRoleSerializer(serializers.Serializer):
    name = serializers.CharField()
    comment = serializers.CharField(required=False)
    permission_group_ids = serializers.ListField(child=serializers.IntegerField())
    permission_module_ids = serializers.ListField(child=serializers.IntegerField())
    permission_action_ids = serializers.ListField(child=serializers.IntegerField())

    def validate(self, data):
        if Role.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError({"field": "name", "message": "Ro'l bu nom bilan allaqachon mavjud"})
        return data
    
    def create(self, validated_data):
        with transaction.atomic():
            permission_group_ids = validated_data.get('permission_group_ids')
            permission_module_ids = validated_data.get('permission_module_ids')
            permission_action_ids = validated_data.get('permission_action_ids')
            role = Role.objects.create(
                name=validated_data.get('name'),
                comment=validated_data.get('comment'),
            )
            permission_groups = PermissionGroup.objects.filter(id__in=permission_group_ids)
            permission_modules = PermissionModule.objects.filter(id__in=permission_module_ids)
            permission_actions = PermissionAction.objects.filter(id__in=permission_action_ids)
            role.permission_groups.set(permission_groups)
            role.permission_modules.set(permission_modules)
            role.permission_actions.set(permission_actions)
            role.save()
            return role