from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WebConfig(AppConfig):
    name = 'web'

    def ready(self):
        print("loading signals")
        import web.signals
