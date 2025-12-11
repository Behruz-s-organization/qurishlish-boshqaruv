# django
from django.urls import path, include

# rest framework 
from rest_framework.routers import DefaultRouter


# accounts
# ------- user ------
from core.apps.accounts.views.user import UserViewSet
from core.apps.accounts.views.user.create import CreateUserApiView
from core.apps.accounts.views.user.list import ListUserApiView
from core.apps.accounts.views.user.update import UpdateUserApiView
from core.apps.accounts.views.user.delete import SoftDeleteUserApiView, HardDeleteUserApiView
# ------- auth ------
from core.apps.accounts.views.auth.login import LoginApiView


urlpatterns = [
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
]

router = DefaultRouter()
router.register("user", UserViewSet)


urlpatterns += router.urls
