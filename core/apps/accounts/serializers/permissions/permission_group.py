# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import PermissionGroup
from core.apps.accounts.serializers.permissions.permission_module import PermissionModuleSerializer


class PermissionGroupSerializer(serializers.ModelSerializer):
    modules = PermissionModuleSerializer(many=True, read_only=True)

    class Meta:
        model = PermissionGroup
        fields = [
            'id', 
            'name', 
            'created_at',
            'modules',
        ]

    
class ListPermissionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionGroup
        fields = [
            'id', 
            'name', 
            'created_at',
        ]
