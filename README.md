# Pilates Center

## Pre-entrega 3 Proyecto Final 

### Alumnos: Mancino Melina, Sandoval Valentin

Se crea un proyecto basado en un centro de Pilates, donde los usuarios podrán ver las reservas de sus clases, crear clases y registrar alumnos.

1- Creamos el proyecto: 
   python3 -m django startproject "PilatesCenter"

2- Creamos la aplicación 
   python manage.py startapp reserves   

3- Creamos un archivo urls.py dentro de la carpeta de la app

4- Seteamos el proyecto, agregando la aplicación en seetings y configurando las urls del proyecto para que se conecten con las urls generales

5- Luego, comenzamos a crear la aplicación.
- Se crea la carpeta static que contiene de forma local el bootstrap.ccs que utilizaremos en nuetro diseño.
- Creamos los 3 modelos de nuestra app: Clase, Reserva y Alumno. Y realizamos la migración para que impacte en la app, mediante python manage.py makemigrations y python manage.py migrate
- Creamos las funciones en las vistas
- Creamos un archivo de forms donde importamos los modelos y creamos 
- Configuramos las urls para que sean vinculadas a los templates
- Configuramos los templates por cada clase
- Generamos un usuario "Admin" pass "123456" con python manage.py createsuperuser --username=admin --email=aa@com.ar

6- 