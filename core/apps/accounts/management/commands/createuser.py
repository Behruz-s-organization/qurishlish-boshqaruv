# pypi 
from getpass import getpass

# django
from django.contrib.auth.management.commands.createsuperuser import Command as SuperUserCommand

# django tenants
from django_tenants.utils import schema_context

# accounts
from core.apps.accounts.models import User
# customers
from core.apps.customers.models import Client


class Command(SuperUserCommand):
    def handle(self, *args, **options):
        while True:
            schema = input("Enter schema name: ")
            
            client = Client.objects.filter(schema_name=schema).first()

            if not client:
                self.stdout.write(self.style.WARNING("Schema not found"))
            else:
                break
        
        while True:
            username = input("Enter username: ")
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING("User already exists"))
            else:
                break
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")

        password = getpass("Enter password: ")

        User.objects.create_superuser(
            password=password,
            username=username,
            client=client,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Superuser created successfully in schema '{schema}'"
            )
        )