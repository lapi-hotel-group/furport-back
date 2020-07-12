from django.apps import AppConfig


class FurportConfig(AppConfig):
    name = "furport"

    def ready(self):
        from . import signals
