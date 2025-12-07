from django.apps import AppConfig


class SharedAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.shared_accounts'

    def ready(self):
        import core.apps.shared_accounts.admin
