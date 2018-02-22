from django.apps import AppConfig


class ArtConfig(AppConfig):
    name = 'art'
    def ready(self):
        import art.signals
