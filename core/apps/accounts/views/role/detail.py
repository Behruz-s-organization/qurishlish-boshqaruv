# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import Role
from core.apps.accounts.serializers.role.detail import RoleSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class RoleApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = RoleSerializer
    queryset = Role.objects.prefetch_related('permission_groups', 'permission_modules', 'permission_actions')
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['role'],
        operation_summary="Get role data via ID",
        responses={
            200: openapi.Response(
                schema=None,
                description="Success",
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Role detail with all data",
                        "data": {
                            "id": 0,
                            "name": "string",
                            "comment": "string",
                            "created_at": "string",
                            "permission_groups": [
                                {
                                    "id": 0,
                                    "name": "string",
                                    "created_at": "string"
                                }
                            ],
                            "permission_modules": [
                                {
                                    "id": 0,
                                    "name": "string",
                                    "created_at": "string"
                                }
                            ],
                            "permission_actions": [
                                {
                                    "id": 0,
                                    "name": "string",
                                    "created_at": "string",
                                }
                            ]
                        }
                    }
                }
            ),
            404: openapi.Response(
                schema=None,
                description="Not found",
                examples={
                    "application/json": {
                        "status_code": 404,
                        "status": "not_found",
                        "message": "Role not found"
                    }
                }
            )
        }
    )
    def get(self, request, id):
        role = Role.objects.filter(id=id).first()
        if not role:
            return self.not_found_response(
                message="Role not found"
            )
        serializer = self.serializer_class(role)
        return self.success_response(
            data=serializer.data,
            message="Role detail with all data"
        )
