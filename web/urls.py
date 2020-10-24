from django.contrib import admin
from django.urls import path

from web.views import (ContactoListView, ContactView, CursoDetailView,
                       CursoListView, IndexView, InscripcionesCreateView, UpdateCurso)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contacto/", ContactView.as_view(), name="contacto"),
    path("lista-de-mensajes/", ContactoListView.as_view(), name="listamensajes"),
    path("cursos/", CursoListView.as_view(), name="listacursos"),
    path("curso/<int:pk>/", CursoDetailView.as_view(), name="detalle_curso"),
    path("inscripciones/<int:pk>/", InscripcionesCreateView.as_view(), name="inscripciones"),
    path("curso/<int:pk>/update", UpdateCurso.as_view(), name="update_curso")
]
