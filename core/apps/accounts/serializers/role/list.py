# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import Role


class ListRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'comment',
            'created_at',
            'updated_at',
        ]