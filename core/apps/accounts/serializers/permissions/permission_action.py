# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import PermissionAction


class PermissionActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionAction
        fields = [
            'id',
            'name',
            'created_at',
        ]