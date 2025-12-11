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
        operation_description="""
        Get a list of all roles in the system, with optional pagination.

        Authentication:
            - Requires a valid Bearer access token.

        Process:
            - Retrieves all roles that are not marked as deleted.
            - Supports pagination using the configured pagination class (limit/offset).
            - Returns serialized role data along with pagination metadata.

        Response:
            - 200 OK: Successfully returns a paginated list of roles.
            - Includes fields: count, next, previous, results.
            - Each role includes id, name, comment, created_at, and updated_at.
            - 500 Internal Server Error: Unexpected error occurred while fetching roles.

        Notes:
            - Only authenticated users can access this endpoint.
            - Roles marked as deleted (`is_deleted=True`) are excluded from the response.
            - Pagination fields (`next` and `previous`) provide URLs to navigate pages if results exceed page limit.

        """,
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
            500: openapi.Response(
                description="Error",
                schema=None,
                examples={
                    "application/json": {
                        "status_code": 500,
                        "status": "error",
                        "message": "Xatolik, Iltimos backend dasturchiga murojaat qiling",
                        "data": "string"
                    }
                }
            ),
        }
    )
    def get(self, request):
        try: 
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
        except Exception as e:
            return self.error_response(
                data=str(e)
            )