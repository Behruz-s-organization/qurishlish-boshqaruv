# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import Role
from core.apps.accounts.serializers.permissions.permission_group import ListPermissionGroupSerializer
from core.apps.accounts.serializers.permissions.permission_module import ListPermissionModuleSerializer
from core.apps.accounts.serializers.permissions.permission_action import PermissionActionSerializer


class RoleSerializer(serializers.ModelSerializer):
    permission_groups = ListPermissionGroupSerializer(many=True, read_only=True)
    permission_modules = ListPermissionModuleSerializer(many=True, read_only=True)
    permission_actions = PermissionActionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'comment',
            'created_at',
            'permission_groups',
            'permission_modules',
            'permission_actions',
        ]