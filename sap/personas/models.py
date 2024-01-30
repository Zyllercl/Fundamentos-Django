from django.db import models

# Create your models here. 
# TIPS: Siempre dejar las clases que no tienen relacion al principio

# Clase de Domicilio
class Domicilio(models.Model):
    # Atributos
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

# Clase de Persona
class Persona(models.Model):
    # Atributos
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    # Relacion de tabla Persona con Domicilio
    # on_delete=models.SET_NULL -> Este parametro permite que cuando se elimine un Domicilio este quede null en la DB
    # on_delete=models.CASCADE  -> Si se elimina un registro en la tabla de domicilio, se eliminara el registro de la tabla Persona
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True) # FK
    
    def __str__(self) -> str:
        return f'Personas {self.id}: {self.nombre} {self.apellido}'