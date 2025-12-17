# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# products
from core.apps.products.models import Folder
from core.apps.products.serializers.folder.create import CreateFolderSerializer
from core.apps.products.serializers.folder.list import ListFolderSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class CreateFolderApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = CreateFolderSerializer
    queryset = Folder.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['products'],
        operation_summary="Create Folder Api for add products",
        responses={
            201: openapi.Response(
                schema=None,
                description="Created",
                examples={
                    "application/json": {
                        "status_code": 201,
                        "status": "created",
                        "message": "Folder successfully created",
                        "data": {
                            "id": 0,
                            "name": "string",
                            "count_products": 0,
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
                        "data": {"field": "string", "message": "stirng"}
                    }
                }
            ),
            500: openapi.Response(
                schema=None,
                description="Failure",
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
                instance = serializer.save()
                return self.created_response(
                    data=ListFolderSerializer(instance).data,
                    message="Folder successfully created"
                )
            return self.failure_response(
                data=serializer.errors,
            )
        except Exception as e:
            return self.error_response(data=str(e))