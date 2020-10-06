from .models import Contacto
<<<<<<< HEAD
from django.db.models.signals import pre_save, post_save
import logging
from datetime import datetime
=======
from django.db.models.signals import pre_save
>>>>>>> added signals dir & config
from django.dispatch import receiver


@receiver(pre_save, sender=Contacto)
<<<<<<< HEAD
def pre_create_contact(sender, instance, **kwargs):
    today = datetime.today().strftime('%d-%m-%y')
    print("Formulario de contacto submiteado!!!!!")
    logging.warning(f"{today} Formulario de contacto submiteado!")


@receiver(post_save, sender=Contacto)
def post_create_contact(sender, instance, **kwargs):
    today = datetime.today().strftime('%d-%m-%y')
    message = f"{today} POST_SAVE Se creo un nuevo contacto."
    logging.warning(message)

post_save.connect(pre_create_contact, sender=Contacto)
pre_save.connect(post_create_contact, sender=Contacto)
=======
def create_contact(sender, instance, **kwargs):
    print("New contact from signals.py")


pre_save.connect(create_contact, sender=Contacto)
>>>>>>> added signals dir & config
