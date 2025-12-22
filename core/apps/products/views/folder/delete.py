# rest framework
from rest_framework import views, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# products
from core.apps.products.models import Folder

# utils
from core.utils.response.mixin import ResponseMixin


class DeleteFolderApiView(views.APIView, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=["product folders"],
        responses={
            204: openapi.Response(
                schema=None,
                description="Deleted",
                examples={
                    "application/json": {
                        "status_code": 204,
                        "status": "deleted",
                        "message": "Folder successfully deleted",
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
                        "message": "Folder not found"
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
                        "data": "string"
                    }
                }
            )
        }
    )
    def delete(self, request, id):
        try:
            folder = Folder.objects.filter(id=id).first()
            if not folder:
                return self.not_found_response("Folder not found")
            folder.is_deleted = True
            folder.save()
            return self.deleted_response(
                message="Folder deleted successfully"
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )