# django
from django.db import transaction

# rest framework
from rest_framework import serializers

# accounts
from core.apps.accounts.models import User, Role


class CreateUserSerializer(serializers.Serializer):
    profile_image = serializers.ImageField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    role_id = serializers.IntegerField()

    def validate(self, data):
        if User.objects.filter(username=data['username'], is_deleted=False).exists():
            raise serializers.ValidationError({"username": "User with this username already exists"})
        role = Role.objects.filter(id=data['role_id'], is_deleted=False).first()
        if not role:
            raise serializers.ValidationError({"role": "Role not found"})
        data['role'] = role
        return data

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                first_name=validated_data.get('first_name'),
                last_name=validated_data.get('last_name'),
                username=validated_data.get('username'),
                phone_number=validated_data.get('phone_number'),
                is_active=validated_data.get('is_active'),
                profile_image=validated_data.get('profile_image'),
                role=validated_data.get('role'),
            )

            user.set_password(validated_data.get('password'))
            user.save()

            return user