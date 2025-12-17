# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import Role, PermissionGroup, PermissionAction, PermissionModule


class UpdateRoleSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    comment = serializers.CharField()
    permission_group_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    permission_module_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    permission_action_ids = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate(self, data):
        if data.get('name'):
            if Role.objects.filter(name=data.get('name')).exists():
                raise serializers.ValidationError({"field": "name", "message": "Ro'l bu nom bilan allaqachon mavjud"})
        return data
    
    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.name = validated_data.get('name', instance.name)
            instance.comment = validated_data.get('comment', instance.comment)
            
            if 'permission_group_ids' in validated_data:
                groups = PermissionGroup.objects.filter(
                    id__in=validated_data['permission_group_ids']
                )
                instance.permission_groups.set(groups)

            if 'permission_module_ids' in validated_data:
                modules = PermissionModule.objects.filter(
                    id__in=validated_data['permission_module_ids']
                )
                instance.permission_modules.set(modules)

            if 'permission_action_ids' in validated_data:
                actions = PermissionAction.objects.filter(
                    id__in=validated_data['permission_action_ids']
                )
                instance.permission_actions.set(actions)

            instance.save()
            return instance