# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


# shared_accounts
from core.apps.shared_accounts.models.user import AdminUser


@admin.register(AdminUser)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active",)
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)