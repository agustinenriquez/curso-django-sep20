from django.contrib import admin
from .models import Curso, Pelicula, Contacto, ImagenCurso
# Register your models here.


class ImagenCursoAdmin(admin.StackedInline):
    model = ImagenCurso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    inlines = [ImagenCursoAdmin]
    exclude = ("imagen", )


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "mayores_de", "preventa_online", "fecha_de_estreno")

    def fecha_de_estreno(self, obj):
        return obj.fecha.strftime("%d-%m-%Y")
    fecha_de_estreno.short_description = "Fecha de estreno"


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("author", "email")


@admin.register(ImagenCurso)
class ImagenCursoAdmin(admin.ModelAdmin):
    class Meta:
        model = ImagenCurso
        fields = '__all__'
