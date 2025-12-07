# rest framework
from rest_framework import viewsets
from rest_framework.decorators import action

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user import user as serializers

# utils
from core.utils.response.mixin import ResponseMixin
from core.utils.permissions.tenant_user import IsTenantUser


class UserViewSet(viewsets.GenericViewSet, ResponseMixin):
    queryset = User.objects.all()
    permission_classes = [IsTenantUser]

    def get_serializer_class(self):
        match self.action:
            case "POST":
                return 
            case ["PUT", "PATCH"]:
                return
            case _:
                return serializers.UserSerializer

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
