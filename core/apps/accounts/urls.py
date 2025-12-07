# django
from django.urls import path, include

# rest framework simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('user/', include(
        [

        ]
    )),
    # ------ authentication ------
    path('auth/', include(
        [
            path('login/', TokenObtainPairView.as_view(), name='login-api'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh-api'),
        ]
    )),
]