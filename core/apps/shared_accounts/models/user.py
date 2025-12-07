# django
from django.db import models
from django.contrib.auth.models import AbstractUser


# shared
from core.apps.shared.models import BaseModel


class AdminUser(AbstractUser, BaseModel):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"        
