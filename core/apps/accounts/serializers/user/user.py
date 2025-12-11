# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username',
            'phone_number',
            'profile_image',
            'created_at',
            'updated_at',
        ]
    

class ListUserSerializer(UserSerializer):
    role = serializers.SerializerMethodField(method_name='get_role')

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + [
            'is_active',
            'role'
        ]

    def get_role(self, obj):
        return {
            'id': obj.role.id,
            'name': obj.role.name,
        } if obj.role else {}