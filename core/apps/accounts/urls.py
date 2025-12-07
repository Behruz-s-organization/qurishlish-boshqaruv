# django
from django.urls import path, include

# rest framework 
from rest_framework.routers import DefaultRouter


# accounts
# ------- user ------
from core.apps.accounts.views.user import UserViewSet
# ------- auth ------
from core.apps.accounts.views.auth.login import LoginApiView


urlpatterns = [
    path('user/', include(
        [

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
