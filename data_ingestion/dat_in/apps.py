from django.apps import AppConfig


class DatInConfig(AppConfig):
    name = 'dat_in'

    def ready(self):
        import dat_in.signals
