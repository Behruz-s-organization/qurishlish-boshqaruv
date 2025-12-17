# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import PermissionModule
from core.apps.accounts.serializers.permissions.permission_action import PermissionActionSerializer


class PermissionModuleSerializer(serializers.ModelSerializer):
    actions = PermissionActionSerializer(many=True, read_only=True)

    class Meta:
        model = PermissionModule
        fields = [
            'id',
            'name',
            'created_at',
            'actions',
        ]
    

class ListPermissionModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionModule
        fields = [
            'id',
            'name',
            'created_at',
        ]