# rest framework
from rest_framework import generics

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User
from core.apps.accounts.serializers.auth import login as serializers
from core.apps.accounts.serializers.user import UserSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class LoginApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = serializers.LoginSerializer
    queryset = User.objects.all()
    
    @swagger_auto_schema(
        tags=["auth"],
        responses={
            200: openapi.Response(
                description="Success",
                schema=None,
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Login muvaffaqiyatli amalga oshirildi",
                        "data": {
                            "user": {
                                "id": 0,
                                "first_name": "string",
                                "last_name": "string",
                                "username": "string",
                                "phone_number": "string",
                                "profile_image": "string",
                                "created_at": "string",
                                "updated_at": "string",
                            },
                            "tokens": {
                                "access_token": "string",
                                "refresh_token": "string",
                            }
                        }
                    }
                }
            )
        }
    )
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data.get('user')
                token = user.get_jwt_token()
                data = {
                    "user": UserSerializer(user).data,
                    "tokens": token,
                }
                return self.success_response(
                    data=data,
                    message="Login muvaffaqiyatli amalga oshirildi"
                )
            return self.failure_response(
                data=serializer.errors,
                message="Kiritayotgan malumotingizni tekshirib ko'ring"
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )
