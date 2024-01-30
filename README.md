# Fundamentos-Django
Fundamentos Django 

# Crear un Entorno Virtual
> py -3 -m venv .venv

## Activar Entorno Virtual
cd .venv\Scripts\
> activate

## Actualizar en Entorno Virtual
> python -m pip install --upgrade pip

# Instalar Django
> python -m pip install django

## Iniciar proyecto en Django
> django-admin startproject 'sap' (Sistema Administracion de Personas )

## Crear una App dentro del proyecto Django
> python manage.py startapp 'webapp'

## Agregar aplicacion creada en el proyecyo principal
- Dirigirse a Settings.py (archivo en la carpeta del proyecto Django)
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        ###     Aplicaciones Creadas     ###
        'webapp',
    ]

## Descripcion de comandos globales:
- python manage.py runserver [Encender el servidor]
- python manage.py migrate [Realiza las migraciones]
- python manage.py makemigrations [Corrobora si hay cambios o no en el modelo]
- python manage.py createsuperuser [Crea el usuario ADMIN del administrador de Django]

# Instalacion de Postgresql
> python -m pip install psycopg2

## Crear una Base de Datos en PostgreSQL
- Nombre: spa_db

## Revisar configuracion en settings.py del proyecto SAP

# Creacion de Clases de Modelo
> python manage.py startapp personas

## Creacion del modelo Persona
- Dirigirse al modulo personas > models.py

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

## Ver la sentencia SQL
- Primero se debe comprobar si hay cambios en el modelo:
> python manage.py makemigrations
- Visualizar sentencia SQL
> python manage.py sqlmigrate personas 0001

## Registrar clase Personas
- Dirigirse a admin.py del modulo de personas, agregar la siguiente linea:

admin.site.register(Persona)
