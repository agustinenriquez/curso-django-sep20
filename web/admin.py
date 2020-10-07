from django.contrib import admin
from .models import Curso, Pelicula, Contacto, AdjuntosCurso
# Register your models here.


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre", "mayores_de", "preventa_online", "fecha_de_estreno")

    def fecha_de_estreno(self, obj):
        return obj.fecha.strftime("%d-%m-%Y")
    fecha_de_estreno.short_description = "Fecha de estreno"


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("author", "email")


class AdjuntosCursoAdmin(admin.StackedInline):
    model = AdjuntosCurso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [AdjuntosCursoAdmin]
    list_display = ("nombre", "precio")
    exclude = ("adjuntos", )


@admin.register(AdjuntosCurso)
class AdjuntosCursoAdmin(admin.ModelAdmin):
    class Meta:
        model = AdjuntosCurso
        fields = '__all__'
