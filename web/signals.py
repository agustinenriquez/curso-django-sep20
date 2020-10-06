from .models import Contacto
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Contacto)
def create_contact(sender, instance, **kwargs):
    print("New contact from signals.py")


pre_save.connect(create_contact, sender=Contacto)
