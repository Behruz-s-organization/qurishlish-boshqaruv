# django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# rest framework
from rest_framework import permissions
# drf yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

description = """
This API provides backend services for the application, allowing users to authenticate, manage their profiles, and interact with various system resources.

Authentication:
- The API uses JWT-based authentication.
- To access protected endpoints, include the header: `Authorization: Bearer <access_token>`.
- Tokens can be obtained from the authentication endpoints (login, refresh).

Request Format:
- All requests must be sent in JSON format unless otherwise specified.
- File uploads should use multipart/form-data.

Response Format:
- All responses follow a unified structure containing:
  - status_code
  - status (success, failure, error, not_found, created, deleted)
  - message
  - data (optional)
- Error responses include detailed validation messages if applicable.

Pagination:
- Pagination is supported using `limit` and `offset` query parameters.
- Default limit and maximum allowed limit may vary per endpoint.

Versioning:
- Current API version: v1.

Notes:
- Some endpoints require elevated permissions (e.g., admin access).
- All timestamps are returned in ISO 8601 format.
- For secure token storage, avoid exposing refresh tokens on client-side environments.

Use this documentation to explore available endpoints, inspect request/response formats, and test API calls interactively.
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Qurilish Boshqaruv API",
      default_version='v1',
      description=description,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="xoliqberdiyevbehruz12@gmail.com"),
      license=openapi.License(name="Behruz's-Organization License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
   path('api/v1/', include(
      [
         path('accounts/', include('core.apps.accounts.urls')),
      ]
   )),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)