# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import Role
from core.apps.accounts.serializers.role.create import CreateRoleSerializer
from core.apps.accounts.serializers.role.list import ListRoleSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class CreateRoleApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = CreateRoleSerializer
    queryset = Role.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['role'],
        operation_summary="Create a new role in the system",
        responses={
            200: openapi.Response(
                schema=None,
                description="Success",
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Role successfully created",
                        "data": {
                            "id": 0,
                            "name": "string",
                            "comment": "string",
                            "created_at": "string",
                            "updated_at": "string"
                        }
                    }
                }
            ),
            400: openapi.Response(
                schema=None,
                description="Failure",
                examples={
                    "application/json": {
                        "status_code": 400,
                        "status": "failure",
                        "message": "Kiritayotgan malumotingizni tekshirib ko'ring",
                        "data": "string"
                    }
                }
            ),
            500: openapi.Response(
                schema=None,
                description="Error",
                examples={
                    "application/json": {
                        "status_code": 500,
                        "status": "error",
                        "message": "Xatolik, Iltimos backend dasturchiga murojaat qiling",
                        "error_message": "string"
                    }
                }
            )
        }
    )
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                return self.created_response(
                    data=ListRoleSerializer(obj).data,
                    message="Role successfully created"
                )
            return self.failure_response(
                data=serializer.errors
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )
