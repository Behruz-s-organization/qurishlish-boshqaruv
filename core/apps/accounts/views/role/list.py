# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import Role
from core.apps.accounts.serializers.role.list import ListRoleSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class ListRoleApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = ListRoleSerializer
    queryset = Role.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['role'],
        operation_summary="Retrieve a paginated list of roles.",
        responses={
            200: openapi.Response(
                description="Succes",
                schema=None,
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Roles list",
                        "data": {
                            "count": 0,
                            "next": "string",
                            "previous": "string",
                            "results": [
                                {
                                    "id": 1,
                                    "name": "string",
                                    "comment": "string",
                                    "created_at": "string",
                                    "updated_at": "string"
                                },
                            ]
                        }
                    }
                }
            ),
        }
    )
    def get(self, request):
        queryset = self.queryset.filter(is_deleted=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.success_response(
                data=self.get_paginated_response(serializer.data).data,
                message="Roles list"
            )
        serializer = self.serializer_class(queryset, many=True)
        return self.success_response(
            data=serializer.data,
            message="Roles list"
        )
