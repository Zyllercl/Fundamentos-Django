from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

# Create your views here.
def bienvenido(request):
    # Despliegue de registros de la DB de Personas
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})