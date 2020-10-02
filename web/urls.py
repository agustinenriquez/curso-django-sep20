from django.contrib import admin
from django.urls import path

from web.views import (aeropuertos_json, consumir_endpoint, htmlpersonalizado,
                       index, respuesta_json, contacto, detallecurso, inscripciones,
                       agregar_peliculas)

urlpatterns = [
    path("", index, name="index"),
    path("holamundo", htmlpersonalizado, name="holamundo"),
    path("endpoint", consumir_endpoint, name="endpoint"),
    path("respuesta_json", respuesta_json, name="respuesta_json"),
    path("aeropuertos/json/", aeropuertos_json, name="aeropuertos_json"),
    path("contacto", contacto, name="contacto"),
    path("curso/<int:pk>/", detallecurso, name="detalle_curso"),
    path("curso/<int:pk>/incripcion/", inscripciones, name="inscripciones"),
    path("peliculas/agregar/", agregar_peliculas, name="agregar_peliculas"),
]
