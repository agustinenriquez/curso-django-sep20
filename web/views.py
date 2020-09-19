import pdb
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import os
import csv
# Create your views here.


def index(request):
    context = {}
    return render(request, "web/index.html", context)


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
