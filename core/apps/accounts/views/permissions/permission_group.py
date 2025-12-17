# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# accounts
from core.apps.accounts.models import PermissionGroup
from core.apps.accounts.serializers.permissions.permission_group import PermissionGroupSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class ListPermissionGroupApiView(generics.GenericAPIView, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PermissionGroup.objects.prefetch_related('modules')
    serializer_class = PermissionGroupSerializer

    @swagger_auto_schema(
        tags=['permissions'],
        operation_summary="Permissions Group, Module and Action list api",
        responses={
            200: openapi.Response(
                schema=None,
                description="Success",
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Permissions list",
                        "data": {
                            "count": 0,
                            "next": "string",
                            "previous": "string",
                            "results": [
                                {
                                    "id": 0,
                                    "name": "string",
                                    "created_at": "string",
                                    "modules": [
                                        {
                                            "id": 0,
                                            "name": "string",
                                            "created_at": "string",
                                            "actions": [
                                                {
                                                    "id": 1,
                                                    "name": "string",
                                                    "created_at": "string"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            )
        }
    )
    def get(self, request):
        queryset = self.queryset.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.success_response(
                data=self.get_paginated_response(serializer.data).data,
                message="Permissions list",
            )
        serializer = self.serializer_class(queryset, many=True)
        return self.success_response(
            data=serializer.data,
            message="Permissions list"
        )
