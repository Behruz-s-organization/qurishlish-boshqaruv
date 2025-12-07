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
    