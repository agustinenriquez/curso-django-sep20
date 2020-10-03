from django.contrib import admin
from django.urls import path

from web.views import (index, contacto, detallecurso, inscripciones,
                       agregar_peliculas, busqueda, logueo, deslogueo, crear_curso,
                       crear_usuario)

urlpatterns = [
    path("", index, name="index"),
    path("contacto/", contacto, name="contacto"),
    path("curso/<int:pk>/", detallecurso, name="detalle_curso"),
    path("curso/<int:pk>/incripcion/", inscripciones, name="inscripciones"),
    path("curso/crear/", crear_curso, name="crear-curso"),
    path("peliculas/agregar/", agregar_peliculas, name="agregar_peliculas"),
    path("busqueda", busqueda, name="busqueda"),
    path("login/", logueo, name="login"),
    path("logout/", deslogueo, name="deslogueo"),
    path("usuario/agregar", crear_usuario, name="crear_usuario"),
    # user/add
    # user/remove
    # user/change
    # profile/userid
]
