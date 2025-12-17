# rest framework 
from rest_framework import serializers


# accounts
from core.apps.accounts.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if not user or (user and not user.check_password(data['password'])):
            raise serializers.ValidationError({"field": "username_and_password", "message": "Username yoki parol noto'g'ri"})
        data['user'] = user
        return data