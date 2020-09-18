from django.contrib import admin
from django.urls import path
from web.views import index, htmlpersonalizado, consumir_endpoint, respuesta_json


urlpatterns = [
    path("", index, name="index"),
    path("holamundo", htmlpersonalizado, name="holamundo"),
    path("endpoint", consumir_endpoint, name="endpoint"),
    path("respuesta_json", respuesta_json, name="respuesta_json")
]
