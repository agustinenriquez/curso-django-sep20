from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.


def index(request):
    return HttpResponse("Hola, mundo!")


def htmlpersonalizado(request):
    respuesta_html = "<h1>Hola, mundo personalizado!</h1>"
    return HttpResponse(respuesta_html)


def respuesta_json(request):
    # Devuelve un json personalizado
    mi_json = {"Nombre": "Agustin"}
    return JsonResponse(json.dumps(mi_json), safe=False)

def consumir_endpoint(request):
    # Devuelve informacion sobre venta y compra a traves de una api externa.
    endpoint = "https://api.recursospython.com/dollar"
    respuesta = requests.get(endpoint)
    precio_compra = respuesta.json()["buy_price"]
    precio_venta = respuesta.json()["sale_price"]
    respuesta_html = f"<p>Precio compra: {precio_compra}. Precio venta: {precio_venta}</p>"
    return HttpResponse(respuesta_html)
