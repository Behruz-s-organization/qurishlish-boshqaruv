# rest framework
from rest_framework import generics, permissions, parsers

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user.create import CreateUserSerializer
from core.apps.accounts.serializers.user.user import UserSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class CreateUserApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    @swagger_auto_schema(
        tags=['user'],
        operation_summary="Api for create employees",
        operation_description="""
        Create a new user account.

        Request Body:
        - Requires user details based on the serializer fields.
        - All required fields must be provided in MULTIPART/DATA format.

        Behavior:
        - Validates the incoming data using the serializer.
        - If validation succeeds, a new user is created and returned.
        - If validation fails, an appropriate error message is returned.

        Response:
        - On success: Returns the newly created user object with a success message.
        - On error: Returns validation or processing error details.
        """,
        responses={
            201: openapi.Response(
                description="Created",
                schema=None,
                examples={
                    "application/json": {
                        "status": "created",
                        "status_code": 201,
                        "message": "User successfully created!",
                        "data": {
                            "id": 0,
                            "first_name": "string",
                            "last_name": "string",
                            "username": "string",
                            "phone_number": "string",
                            "profile_image": "string",
                            "created_at": "string",
                            "updated_at": "string",
                        } 
                    }
                }
            ),
            400: openapi.Response(
                description="Failure",
                schema=None,
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
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                return self.created_response(
                    data=UserSerializer(user).data,
                    message="User successfully created!"
                )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )