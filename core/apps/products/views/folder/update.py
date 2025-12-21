# rest framework
from rest_framework import generics, permissions

# drf yasg 
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# products
from core.apps.products.models import Folder
from core.apps.products.serializers.folder.update import UpdateFolderSerializer
from core.apps.products.serializers.folder.list import ListFolderSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class UpdateFolderApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UpdateFolderSerializer
    queryset = Folder.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['product folders'],
        responses={
            200: openapi.Response(
                schema=None,
                description="Success",
                examples={
                    "application/json": {
                        "status_code": 200,
                        "status": "success",
                        "message": "Product folder successfully updated",
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
                        "data": "string"
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
                        "message": "Folder not found with this id",
                    }
                }
            ),
            500: openapi.Response(
                schema=None,
                description="Server Error",
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
    def patch(self, request, id):
        try:
            folder = Folder.objects.filter(id=id, is_deleted=False).first()
            if not folder:
                return self.not_found_response(message="Folder not found with this id")
            serializer = self.serializer_class(data=request.data, instance=folder)
            if serializer.is_valid():
                instance = serializer.save()
                return self.success_response(
                    data=ListFolderSerializer(instance).data,
                    message="Product folder successfully updated",
                )
            return self.failure_response(
                data=serializer.errors,
            )
        except Exception as e:
            return self.error_response(
                data=str(e),
            )