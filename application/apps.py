from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    name = "application"

    def ready(self):
        import application.signals
