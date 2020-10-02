from django.contrib import admin
from .models import Curso, Pelicula
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "preventa_online", "mayores_de", "fecha_de_estreno")

    def fecha_de_estreno(self, obj):
        return obj.fecha_estreno.strftime("%d-%m-%Y")
    fecha_de_estreno.short_description = 'Fecha de estreno'    
