# rest framework
from rest_framework import generics, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import Role
from core.apps.accounts.serializers.role.update import UpdateRoleSerializer
from core.apps.accounts.serializers.role.list import ListRoleSerializer

# utils
from core.utils.response.mixin import ResponseMixin


class UpdateRoleApiView(generics.GenericAPIView, ResponseMixin):
    serializer_class = UpdateRoleSerializer
    queryset = Role.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['role'],
        operation_summary="",
        operation_description="""
        
        """,
        responses={}
    )
    def patch(self, request, id):
        try:
            instance = Role.objects.filter(id=id).first()
            if not instance:
                return self.not_found_response(data={}, message="Role not found with this id")
            serializer = self.serializer_class(data=request.data, instance=instance, partial=True)
            if serializer.is_valid():
                updated_instance = serializer.save()
                return self.success_response(
                    data=ListRoleSerializer(updated_instance).data,
                    message="Role successfully updated"
                )
            return self.failure_response(
                data=serializer.errors,
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )
        


