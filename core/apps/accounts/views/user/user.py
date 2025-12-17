# rest framework
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user import user as serializers

# utils
from core.utils.response.mixin import ResponseMixin


class UserViewSet(viewsets.GenericViewSet, ResponseMixin):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        match self.action:
            case "POST":
                return 
            case ["PUT", "PATCH"]:
                return
            case _:
                return serializers.UserSerializer
    
    @swagger_auto_schema(
        tags=['user'],
        operation_summary="Get currently authenticated user's profile",
        responses={
            200: openapi.Response(
                description="Success",
                schema=None,
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "User ma'lumotlari",
                        "data": {
                            "id": 0,
                            "first_name": "string",
                            "last_name": "string",
                            "username": "string",
                            "phone_number": "+998951234567",
                            "profile_image": None or "string",
                            "created_at": "string",
                            "updated_at": "string"
                        }
                    }
                }
            ),
        }        
    )
    @action(
        methods=["GET"], url_name="me", url_path="me", detail=False
    )
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return self.success_response(
            data=serializer.data,
            message="User ma'lumotlari"
        )
