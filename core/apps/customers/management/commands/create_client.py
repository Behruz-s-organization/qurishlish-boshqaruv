from django.core.management import BaseCommand

from core.apps.customers.models import Client, Domain

class Command(BaseCommand):
    def handle(self, *args, **options):
        client_name = input('Mijoz nomini kiriting: ')
        schema_name = input('Schema nomini kiriting: ').lower()
        domain = input('Domain kiriting: ').lower()

        client, created = Client.objects.get_or_create(
            name=client_name,
            schema_name=schema_name,
        )
        Domain.objects.get_or_create(
            domain=domain,
            tenant=client,
            is_primary=True
        )

        self.stdout("Mijoz qo'shildi")
        