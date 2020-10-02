from django.http.response import JsonResponse
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import os
import csv
from .models import Curso
from .forms import CursoForm, FormularioCursos, PeliculaForm
# Create your views here.


def index(request):
    cursos = Curso.objects.all()
    return render(request, "web/index.html", {"cursos": cursos})

def detallecurso(request, *args, **kwargs):
    """
        Devuelve el detalle de un curso usando la pk definida en urls.py.
    """
    curso = Curso.objects.get(pk=kwargs['pk'])
    formu = CursoForm()
    return render(request, "web/detalle_curso.html", {"curso": curso, "formu": formu})

def inscripciones(request, *args, **kwargs):
    if request.method == 'POST':
        formu = FormularioCursos(request.POST)
        if formu.is_valid():
            formu.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "web/inscripciones.html", {"form": formu, "error": formu.errors})
    else:
        formu = FormularioCursos()
        return render(request, "web/inscripciones.html", {"form": formu})


def htmlpersonalizado(request):
    respuesta_html = "<h1>Hola, mundo personalizado!</h1>"
    return HttpResponse(respuesta_html)


def respuesta_json(request):
    # Devuelve un json personalizado
    mi_json = {"Nombre": "Agustin"}
    return JsonResponse(json.dumps(mi_json), safe=False)

def consumir_endpoint(request):
    # Ejercicio 1
    # Devuelve informacion sobre venta y compra a traves de una api externa.
    endpoint = "https://api.recursospython.com/dollar"
    respuesta = requests.get(endpoint)
    precio_compra = respuesta.json()["buy_price"]
    precio_venta = respuesta.json()["sale_price"]
    respuesta_html = f"<p>Precio compra: {precio_compra}. Precio venta: {precio_venta}</p>"
    return HttpResponse(respuesta_html)

def aeropuertos_json(request):
    ruta_archivo = os.path.dirname(os.path.abspath(__file__)) + "/aeropuertos.csv"
    lista_aeropuertos = []
    with open(ruta_archivo, mode="r") as archivo:
        aeropuertos = csv.reader(archivo, delimiter=",")
        for aeropuerto in aeropuertos:
            item = {}
            item['ciudad'] = aeropuerto[0]
            item['estado'] = aeropuerto[1]
            item['lat'] = aeropuerto[2]
            item['lon'] = aeropuerto[3]
            lista_aeropuertos.append(item)
    return JsonResponse(json.dumps(lista_aeropuertos), safe=False)

def contacto(request):
    unalista = [1,2,5,32,1,7,4545]
    context = {"Nombre": "Agustin", "Profesion": "Ingeniero en sistemas", "unalista": unalista}
    return render(request, "web/contacto.html", context)

def nueva_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("agregar_peliculas"))
    else:
        form = PeliculaForm()
    return render(request, "web/pelicula.html", {'form': form})
