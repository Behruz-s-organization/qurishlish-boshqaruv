# django
from django.urls import path, include


# products
# ------ folder ------
from core.apps.products.views.folder.create import CreateFolderApiView
from core.apps.products.views.folder.list import ListFolderApiView
from core.apps.products.views.folder.update import UpdateFolderApiView


urlpatterns = [
    # ------ folder ------
    path('folder/', include(
        [
            path('create/', CreateFolderApiView.as_view(), name='create-folder-api'),
            path('list/', ListFolderApiView.as_view(), name='list-folder-api'),
            path('<int:id>/update/', UpdateFolderApiView.as_view(), name='update-folder-api'),
        ]
    )),
]