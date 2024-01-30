from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render

from personas.models import Persona
from personas.forms import PersonaForm

# Create your views here.

# Detalle de Persona
def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id) # Redireccionamiento a Not Found 404
    return render(request, 'personas/detalle.html', {'persona': persona})

# Creacion de Formulario Persona
# PersonaForm = modelform_factory(Persona, exclude=[])

# Crear una nueva Persona
def nuevaPersona(request):
    if request.method == 'POST':
        # Obtencion de todos los parametros del formulario
        formaPersona = PersonaForm(request.POST)
        # Validacion del formulario
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')     
    else:
        # Formulario persona vacio
        formaPersona = PersonaForm()

    # Redireccion al formulario
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

# Editar una nueva Persona
def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id) # Redireccionamiento a Not Found 404
    if request.method == 'POST':
        # Obtencion de todos los parametros del formulario
        formaPersona = PersonaForm(request.POST, instance=persona)
        # Validacion del formulario
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')     
    else:
        # Recuperar la persona a editar
        formaPersona = PersonaForm(instance=persona)

    # Redireccion al formulario
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


# Eliminar una nueva Persona
def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id) # Redireccionamiento a Not Found 404
    
    if persona:
        persona.delete()
    
    return redirect('inicio')