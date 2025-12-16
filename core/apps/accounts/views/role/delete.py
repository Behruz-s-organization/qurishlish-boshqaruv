# rest framework
from rest_framework import views, permissions

# drf yasg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# accounts
from core.apps.accounts.models.role import Role

# utils
from core.utils.response.mixin import ResponseMixin


class SoftDeleteRoleApiView(views.APIView, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        tags=['role'],
        operation_summary="Soft delete role with id",
    )
    def delete(self, request, id):
        try:
            role = Role.objects.filter(id=id).first()
            if not role:
                return self.not_found_response(message="Role not found with this id")
            role.is_deleted = True
            role.save()
            return self.deleted_response(message="Role deleted")
        except Exception as e:
            return self.error_response(data=str(e))



class HardDeleteRoleApiView(views.APIView, ResponseMixin):
        permission_classes = [permissions.IsAuthenticated]
        
        @swagger_auto_schema(
            tags=['role'],
                operation_summary="Hard delete role with id",
            )
        def delete(self, request, id):
            try:
                role = Role.objects.filter(id=id).first()
                if not role:
                    return self.not_found_response(message="Role not found with this id")
                role.delete()
                return self.deleted_response(message="Role deleted")
            except Exception as e:
                return self.error_response(data=str(e))
