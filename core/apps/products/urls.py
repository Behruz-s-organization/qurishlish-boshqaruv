# django
from django.urls import path, include


# products
# ------ folder ------
from core.apps.products.views.folder.create import CreateFolderApiView


urlpatterns = [
    # ------ folder ------
    path('folder/', include(
        [
            path('create/', CreateFolderApiView.as_view(), name='create-folder-api'),
        ]
    )),
]