# rest framework
from rest_framework.permissions import BasePermission


class IsTenantUser(BasePermission):
    """
    Allow access only if request.tenant_user exists.
    """

    def has_permission(self, request, view):
        
        return bool(request.tenant_user)