from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    horario = models.CharField(max_length=50, blank=False)
    tags = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField(default=0)
    imagen_principal = models.ImageField(
        upload_to="adjuntos/", default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    mayores_de = models.IntegerField(default=0)
    preventa_online = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    author = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=350)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.author


class AdjuntosCurso(models.Model):
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='adjuntos/')
    nombre = models.CharField(max_length=50, default=None)

    def __str__(self) -> str:
        return self.nombre


@receiver(post_save, sender=Contacto)
def create_contact(sender, instance, created, **kwargs):
    print("New contact and email was sent!")


post_save.connect(create_contact, sender=Contacto)
