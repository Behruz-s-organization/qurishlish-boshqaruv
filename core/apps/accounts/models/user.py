# django
from django.db import models
from django.contrib.auth.models import AbstractUser

# rest framework simplejwt
from rest_framework_simplejwt.tokens import RefreshToken


# shared
from core.apps.shared.models import BaseModel

# customers
from core.apps.customers.models import Client

# utils
from core.utils.validators.phone_number import uz_phone_validator


class User(AbstractUser, BaseModel):
    profile_image = models.ImageField(upload_to="user/profile_images/", null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, validators=[uz_phone_validator]
    )
    groups = None
    user_permissions = None

    def __str__(self):
        return f"#{self.id}: {self.first_name} {self.last_name}"

    @property
    def get_jwt_token(self):
        token = RefreshToken.for_user(self)
        return {
            "access_token": str(token.access_token),
            "refresh_token": str(token), 
        }

    def delete(self, *args, **kwargs):
        if self.profile_image:
            self.profile_image.delete(save=False)
        return super().delete(*args, **kwargs)