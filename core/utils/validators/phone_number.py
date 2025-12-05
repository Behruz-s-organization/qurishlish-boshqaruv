# django
from django.core.validators import RegexValidator

uz_phone_validator = RegexValidator(
    regex=r"^\+998\d{9}$",
    message="The phone_number is invalid. The format should be like this: +998XXXXXXXXX"
)