from django.contrib import admin
from django.urls import path

from web.views import (index, contacto, detallecurso, inscripciones,
                       agregar_peliculas)

urlpatterns = [
    path("", index, name="index"),
    path("contacto/", contacto, name="contacto"),
    path("curso/<int:pk>/", detallecurso, name="detalle_curso"),
<<<<<<< HEAD
    path("curso/<int:pk>/incripcion/", inscripciones, name="inscripciones"),
    path("peliculas/agregar/", agregar_peliculas, name="agregar_peliculas"),
=======
    path("curso/<int:pk>/inscripcion/", inscripciones, name="inscripciones")
>>>>>>> 1ba0c17fbcaf9cefff3f08e95200326dba0194c3
]
