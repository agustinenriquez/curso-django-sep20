from django.contrib import admin
from django.urls import path

from web.views import (aeropuertos_json, consumir_endpoint, htmlpersonalizado,
                       index, respuesta_json, contacto, detallecurso, inscripciones,
                       nueva_pelicula)

urlpatterns = [
    path("", index, name="index"),
    path("holamundo", htmlpersonalizado, name="holamundo"),
    path("endpoint", consumir_endpoint, name="endpoint"),
    path("respuesta_json", respuesta_json, name="respuesta_json"),
    path("aeropuertos/json/", aeropuertos_json, name="aeropuertos_json"),
    path("contacto", contacto, name="contacto"),
    path("curso/<int:pk>/", detallecurso, name="detalle_curso"),
    path("curso/<int:pk>/inscripcion/", inscripciones, name="inscripciones"),
    path("pelicula/agregar/", nueva_pelicula, name="agregar_peliculas")
]
