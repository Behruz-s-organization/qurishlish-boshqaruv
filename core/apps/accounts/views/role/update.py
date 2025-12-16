# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import Role
from core.apps.accounts.serializers.role.update import UpdateRoleSerializer
from core.apps.accounts.serializers.role.list import ListRoleSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class UpdateRoleApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UpdateRoleSerializer
    queryset = Role.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['role'],
        operation_summary="Update Role via id",
        responses={
            200: openapi.Response(
                schema=None,
                description="Success",
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Role successfully updated",
                        "data": {
                            "id": 0,
                            "name": "string",
                            "comment": "string",
                            "created_at": "string",
                            "updated_at": "string",
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
            404: openapi.Response(
                schema=None,
                description="Not Found",
                examples={
                    "application/json": {
                        "status_code": 404,
                        "status": "not_found",
                        "message": "Role not found with this id",
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
                        "data": "string"
                    }
                }
            )
        }
    )
    def patch(self, request, id):
        try:
            instance = Role.objects.filter(id=id).first()
            if not instance:
                return self.not_found_response(data={}, message="Role not found with this id")
            serializer = self.serializer_class(data=request.data, instance=instance, partial=True)
            if serializer.is_valid():
                updated_instance = serializer.save()
                return self.success_response(
                    data=ListRoleSerializer(updated_instance).data,
                    message="Role successfully updated"
                )
            return self.failure_response(
                data=serializer.errors,
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )
        


