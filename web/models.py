from django.db import models
# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    horario = models.CharField(max_length=50, blank=False)
    tags = models.CharField(max_length=50, blank=False)
    precio = models.IntegerField(default=0)
<<<<<<< HEAD
    imagen_principal = models.ImageField(
        upload_to="adjuntos/", default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class ImagenCurso(models.Model):
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)
    archivo = models.FileField(upload_to="adjuntos/")
    nombre = models.CharField(max_length=50, default=None, null=True, blank=True)
=======
    imagen = models.ImageField(upload_to="web/static/img/", default=None, null=True, blank=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)
>>>>>>> dinamically setting href onclick img url

    def __str__(self):
        return self.nombre

<<<<<<< HEAD

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    mayores_de = models.IntegerField(default=0)
    preventa_online = models.BooleanField(default=False)


class Contacto(models.Model):
    author = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=350)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.author

=======
    def save(self, *args, **kwargs):
        self.image_path = self.imagen.url.replace("/web", "")
        return super().save(*args, **kwargs)
>>>>>>> dinamically setting href onclick img url
