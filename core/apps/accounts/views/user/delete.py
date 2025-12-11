# rest framework
from rest_framework import views, permissions

# drf yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# accounts
from core.apps.accounts.models import User

# utils
from core.utils.response.mixin import ResponseMixin


class SoftDeleteUserApiView(views.APIView, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['user'],
        operation_summary="Soft delete a user by ID",
        operation_description="""
        Mark a user as deleted without permanently removing them from the database.

        Authentication:
            - Requires a valid Bearer access token.

        Process:
            - The system retrieves the user by the provided ID.
            - If the user exists, the `is_deleted` flag is set to True.
            - The user record remains in the database but is considered inactive/deleted.

        Response:
            - 200 OK: User successfully soft deleted.
            - 404 Not Found: No user found with the given ID.
            - 500 Internal Server Error: Unexpected error occurred during deletion.

        Notes:
            - This endpoint only marks the user as deleted and does not remove related data.
            - Only authenticated users with proper permissions can perform this action.
        """,
    )
    def delete(self, request, id):
        try: 
            user = User.objects.filter(id=id).first()
            if not user:
                return self.not_found_response(message="User not found with this id")
            user.is_deleted = True
            user.save()
            return self.deleted_response(
                message="User successfully deleted",
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )
        



class HardDeleteUserApiView(views.APIView, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['user'],
        operation_summary="Permanently delete a user by ID.",
        operation_description="""
        Permanently remove a user from the database by their ID.

        Authentication:
            - Requires a valid Bearer access token.

        Process:
            - The system retrieves the user by the provided ID.
            - If the user exists, the user record is permanently deleted from the database.

        Response:
            - 200 OK: User successfully deleted.
            - 404 Not Found: No user found with the given ID.
            - 500 Internal Server Error: Unexpected error occurred during deletion.

        Notes:
            - This action permanently removes the user and cannot be undone.
            - Only authenticated users with proper permissions can perform this action.
            - All related data handling (foreign keys, constraints) depends on the database setup.
        """,
    )
    def delete(self, request, id):
        try: 
            user = User.objects.filter(id=id).first()
            if not user:
                return self.not_found_response(message="User not found with this id")
            user.delete()
            return self.deleted_response(
                message="User successfully deleted",
            )
        except Exception as e:
            return self.error_response(
                data=str(e)
            )