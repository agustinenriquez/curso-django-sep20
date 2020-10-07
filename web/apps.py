from django.apps import AppConfig


class WebConfig(AppConfig):
    name = 'web'

    def ready(self):
        print("loading signals")
        import web.signals
