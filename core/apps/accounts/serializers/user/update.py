# django
from django.db import transaction

# rest framework
from rest_framework import serializers


# accounts
from core.apps.accounts.models import User, Role


class UpdateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    role_id = serializers.IntegerField()
    phone_number = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    is_active = serializers.BooleanField(default=True)
    profile_image = serializers.ImageField(required=False)

    def validate(self, data):
        role = Role.objects.filter(id=data['role_id']).first()
        if not role:
            raise serializers.ValidationError({"field": "role_id", "message": "Ro'l topilmadi"})
        if data.get('username'):
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError({"field": "username", "message": "Foydalanuvchi bu username bilan allaqachon mavjud"})
        data['role'] = role
        return data
    
    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.role = validated_data.get('role', instance.role)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.username = validated_data.get('username', instance.username)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.profile_image = validated_data.get('profile_image', instance.profile_image)

            if validated_data.get('password'):
                instance.set_password(validated_data.get('password'))
            
            instance.save()
            return instance