# django
from django.urls import path, include

# rest framework 
from rest_framework.routers import DefaultRouter


# accounts
# ------- user -------
from core.apps.accounts.views.user import UserViewSet
from core.apps.accounts.views.user.create import CreateUserApiView
from core.apps.accounts.views.user.list import ListUserApiView
from core.apps.accounts.views.user.update import UpdateUserApiView
from core.apps.accounts.views.user.delete import SoftDeleteUserApiView, HardDeleteUserApiView
# ------- auth -------
from core.apps.accounts.views.auth.login import LoginApiView
# ------- role -------
from core.apps.accounts.views.role.create import CreateRoleApiView
from core.apps.accounts.views.role.list import ListRoleApiView
from core.apps.accounts.views.role.update import UpdateRoleApiView
from core.apps.accounts.views.role.delete import HardDeleteRoleApiView, SoftDeleteRoleApiView
from core.apps.accounts.views.role.detail import RoleApiView
# ------- permission -------
from core.apps.accounts.views.permissions.permission_group import ListPermissionGroupApiView


urlpatterns = [
    # ------ user ------
    path('user/', include(
        [
            path('create/', CreateUserApiView.as_view(), name='user-create-api'),
            path('list/', ListUserApiView.as_view(), name='user-list-api'),
            path('<int:id>/update/', UpdateUserApiView.as_view(), name='user-update-api'),
            path('<int:id>/soft_delete/', SoftDeleteUserApiView.as_view(), name='user-soft-delete-api'),
            path('<int:id>/hard_delete/', HardDeleteUserApiView.as_view(), name='user-soft-delete-api'),
        ]
    )),
    # ------ authentication ------
    path('auth/', include(
        [
            path('login/', LoginApiView.as_view(), name='login'),
        ]
    )),
    # ------ role ------
    path('role/', include(
        [
            path('create/', CreateRoleApiView.as_view(), name='create-role-api'),
            path('list/', ListRoleApiView.as_view(), name='list-role-api'),
            path('<int:id>/update/', UpdateRoleApiView.as_view(), name='update-role-api'), 
            path('<int:id>/soft_delete/', SoftDeleteRoleApiView.as_view(), name='soft-delete-role-api'),
            path('<int:id>/hard_delete/', HardDeleteRoleApiView.as_view(), name='hard-delete-role-api'),
            path('<int:id>/', RoleApiView.as_view(), name='role-api'),
        ]
    )),
    # ------ permission ------
    path('permission/', include(
        [
            path('list/', ListPermissionGroupApiView.as_view(), name='list-permissions-api'),
        ]
    )),
]

router = DefaultRouter()
router.register("user", UserViewSet)


urlpatterns += router.urls
