from django.apps import AppConfig


class FetchfromapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fetchFromApi'
    def ready(self):
        from scheduler import scheduler
        scheduler.start()