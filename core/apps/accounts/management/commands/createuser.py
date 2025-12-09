# python
from getpass import getpass

# django
from django.core.management import BaseCommand

# django tenants 
from django_tenants.utils import schema_context


# accounts
from core.apps.accounts.models import User

# customers
from core.apps.customers.models import Client


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = None
        username = None

        while True:
            schema_name = input("Schema nomini kiriting: ")
            client = Client.objects.filter(schema_name=schema_name).first()
            if not client:
                self.stdout.write("Schema topilmadi")
            else: break
        
        with schema_context(schema_name):
            while True:
                username = input("username kiriting: ")
                user = User.objects.filter(username=username).first()
                if user:
                    self.stdout.write("Foydalanuvchi bu username bilan mavjud")
                else:
                    break
            
            first_name = input("Ism kiriting: ")
            last_name = input("Familiya kiriting: ")
            phone_number = input("Telefon raqam kiriting: ")
            password = getpass("Parol kiriting: ")

            User.objects.create_superuser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                phone_number=phone_number,
            )
        
        self.stdout.write("Foydalanuvchi qo'shildi")
