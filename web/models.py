from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    horario = models.CharField(max_length=50, blank=False)
    tags = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="web/static/img/", default=None, null=True, blank=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.image_path = self.imagen.url.replace("/web", "")
        return super().save(*args, **kwargs)


class Pelicula(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    fecha_estreno = models.DateField(auto_now=False, auto_now_add=False)
    mayores_de = models.IntegerField(default=0)
    preventa_online = models.BooleanField(default=False)
