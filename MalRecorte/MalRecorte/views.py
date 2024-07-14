from django.template import Template, Context
from django.http import HttpResponse

import datetime

def saludar(request):
    saludo = "Bienvenido a la Comisión 57810 - Clases de DJango"
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    saludo = f"Te damos la bienvenida a la comisión 57810 {apellido}, {nombre}"
    return HttpResponse(saludo)

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    saludo = f"""
    <html>
    <h1> Bienvenido </h1>
    <h2> Te damos la Bienvenida {apellido}, {nombre} </h2>
    <h3> Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    with open("E:/Estudios/CoderHouse/Python/EntregaFinal/MalRecorte/MalRecorte/Plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)

    return HttpResponse(saludo)