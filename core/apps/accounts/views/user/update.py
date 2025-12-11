# rest framework
from rest_framework import generics, permissions, parsers

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user.update import UpdateUserSerializer
from core.apps.accounts.serializers.user.user import UserSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class UpdateUserApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    @swagger_auto_schema(
        tags=['user'],
        operation_summary="Api for update user with id",
        operation_description="""
        Update the information of an existing user using their ID.

        Authentication:
            - Requires a valid Bearer access token.

        Process:
            - The system retrieves the user by the provided ID.
            - If the user exists, the incoming data is validated using the UpdateUserSerializer.
            - Valid fields are updated and saved.
            - Returns the updated user data on success.

        Request:
            - Accepts partial user data (PATCH).
            - Request format is multipart/form-data
            - Fields can include first_name, last_name, username, phone_number, profile_image, and others defined in the serializer.

        Response:
            - 200 OK: Successfully updates and returns the updated user information.
            - 400 Bad Request: Returned when input validation fails.
            - 404 Not Found: Returned when there is no user associated with the given ID.
            - 500 Internal Server Error: Returned when an unexpected error occurs.

        Notes:
            - Only authenticated users can access this endpoint.
            - Supports partial updates, meaning not all fields are required.
        """,
        responses={
            200: openapi.Response(
                schema=None,
                description="Success",
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "User successfully updated",
                        "data": {
                            "id": 0,
                            "first_name": "sting",
                            "last_name": "sting",
                            "phone_number": "sting",
                            "username": "sting",
                            "profile_image": "sting",
                            "created_at": "sting",
                            "updated_at": "sting",
                        }
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
                        "message": "User not found with given id",
                        "data": {}
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
                        "data": "string",
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
                        "data": "string",
                    }
                }
            ),
        }
    )
    def patch(self, request, id):
        try:
            instance = User.objects.filter(id=id).first()
            if not instance:
                return self.not_found_response(data={}, message="User not found with given id")
            serializer = self.serializer_class(
                data=request.data, instance=instance, partial=True
            )
            if serializer.is_valid():
                updated_instance = serializer.save()
                return self.success_response(
                    data=UserSerializer(updated_instance).data,
                    message="User successfully updated"
                )
            return self.failure_response(
                data=serializer.errors,
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )