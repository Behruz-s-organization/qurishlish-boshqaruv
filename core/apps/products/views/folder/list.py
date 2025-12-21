# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# products
from core.apps.products.models import Folder
from core.apps.products.serializers.folder.list import ListFolderSerializer 

# utils
from core.utils.response.mixin import ResponseMixin


class ListFolderApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = ListFolderSerializer
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
                        "message": "Product folder list",
                        "data": [
                            {
                                "id": 0,
                                "name": "string",
                                "count_products": 0,
                                "created_at": "string",
                                "updated_at": "string",
                            }
                        ]
                    }
                }
            )
        }
    )
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return self.success_response(
            data=serializer.data,
            message="Product folder list",
        )
        