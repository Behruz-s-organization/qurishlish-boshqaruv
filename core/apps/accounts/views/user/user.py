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
        operation_description="""
        Get information about the currently authenticated user.

        Authentication:
            - This endpoint requires an active Bearer access token.

        Process:
            - The system retrieves the user associated with the provided token.
            - The user's information is serialized using the configured serializer.
            - Returns the authenticated user's profile data.

        Response:
            - 200 OK: Successfully returns user details.
            - 401 Unauthorized: Authorization header is missing or token is invalid.
            - 500 Internal Server Error: An unexpected error occurred.

        Notes:
            - This endpoint does not require any request parameters.
            - Useful for fetching the current user's profile without needing an ID.
        """,
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
            500: openapi.Response(
                description="Error",
                schema=None,
                examples={
                    "application/json": {
                        "status_code": 500,
                        "status": "error",
                        "message": "Xatolik, Iltimos backend dasturchiga murojaat qiling",
                        "data": "string",
                    }
                }
            ),
        }        
    )
    @action(
        methods=["GET"], url_name="me", url_path="me", detail=False
    )
    def me(self, request):
        try:
            serializer = self.get_serializer(request.user)
            return self.success_response(
                data=serializer.data,
                message="User ma'lumotlari"
            )
        except Exception as e:
            return self.error_response(
                data=str(e),
            )
