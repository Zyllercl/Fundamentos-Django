
from django.forms import EmailInput, ModelForm

from personas.models import Persona


class PersonaForm(ModelForm):
    
    class Meta:
        model = Persona # Clase de modelo a utilizar
        fields = '__all__'

        widgets = {
            # Personalizacion de la caja de texto, haciendo referencia a que es de tipo Email
            'email': EmailInput(attrs={'type': 'email'})
        }