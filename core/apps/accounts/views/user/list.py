# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user import ListUserSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class ListUserApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = ListUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['user'],
        operation_summary="Api for get list of employees",
        responses={
            200: openapi.Response(
                description="Success",
                schema=None,
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Users list",
                        "data": {
                            "count": 0,
                            "next": "string",
                            "previous": "string",
                            "results": [
                                {
                                    "id": 0,
                                    "first_name": "string",
                                    "last_name": "string",
                                    "username": "string",
                                    "phone_number": "string",
                                    "profile_image": "string",
                                    "created_at": "string",
                                    "updated_at": "string",
                                    "is_active": True,
                                    "role": {
                                        "id": 0,
                                        "name": "string",
                                    },
                                }
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
            )
        },
        manual_parameters=[],
    )
    def get(self, request):
        try:
            queryset = self.queryset.select_related('role')
            page = self.paginate_queryset(queryset)
            print(page)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.success_response(
                    data=self.get_paginated_response(serializer.data).data,
                    message="Users list"
                )
            serializer = self.serializer_class(queryset, many=True)
            return self.success_response(
                data=serializer.data,
                message="Users list"
            )
        except Exception as e:
            return self.error_response(
                data=str(e),
            )
