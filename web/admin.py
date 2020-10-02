from django.contrib import admin
from .models import Curso, Pelicula
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'preventa_online', "fecha_estreno", "mayores_de")

