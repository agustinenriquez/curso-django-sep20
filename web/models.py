from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    horario = models.CharField(max_length=50, blank=False)
    tags = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="web/static/img/", default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre
