from django.contrib import admin
from django.urls import path

from web.views import (index, contacto, detallecurso, inscripciones,
                       agregar_peliculas, logueo, deslogueo)

urlpatterns = [
    path("", index, name="index"),
    path("contacto/", contacto, name="contacto"),
    path("curso/<int:pk>/", detallecurso, name="detalle_curso"),
    path("curso/<int:pk>/incripcion/", inscripciones, name="inscripciones"),
    path("peliculas/agregar/", agregar_peliculas, name="agregar_peliculas"),
    path("login/", logueo, name="logueo"),
    path("logout/", deslogueo, name="deslogueo"),

]
