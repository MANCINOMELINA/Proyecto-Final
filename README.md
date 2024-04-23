## Pre-entrega 3 Proyecto Final 

### Alumnos: Mancino Melina, Sandoval Valentín

Se crea un proyecto basado en un centro de Pilates, donde los usuarios podrán ver las reservas de sus clases, crear clases y registrar alumnos.

1- Creamos el proyecto: 
   python3 -m django startproject "PilatesCenter"

2- Creamos la aplicación 
   python manage.py startapp "reserves"   

3- Creamos un archivo urls.py dentro de la carpeta de la app

4- Configuramos el proyecto, agregando la aplicación en seetings y configurando las urls del proyecto para que se conecten con las urls generales

5- Luego, comenzamos a crear la aplicación.
- Se crea la carpeta static que contiene de forma local el bootstrap.ccs que utilizaremos en nuestro diseño.
- Creamos los 4 modelos de nuestra app: Profesor, Suplente, Clase y Estado. Y realizamos la migración para que impacte en la app, mediante python manage.py makemigrations seguido de python manage.py migrate
- Creamos las funciones en las vistas
- Creamos un archivo de forms donde importamos los modelos y creamos 
- Configuramos las urls para que sean vinculadas a los templates
- Configuramos los templates por cada clase

6- Generamos un usuario "Admin" pass "123456" con python manage.py createsuperuser --username=admin --email=aa@com.ar

7- Accedemos a la app corriendo el servidor mediante python manage.py runserver http://127.0.0.1:8000/ donde se encuentra el home de la web.

8- Para ingresar al menú de opciones ingresamos un la url http://127.0.0.1:8000/reserves/ en la misma, se visualiza un mensaje de bienvenida y los accesos a Reservas, Admin, Crear Reservas y Crear Profesor.

9- Ingresando a Reservas, se aperturará una tarjeta que muestre el resumen de los datos registrados. Ej.: en la parte superior se encuentra el nombre del profesor y el suplente, en el medio el nivel de la clase reservada, abajo una observación particular del alumno para que el profesor considere antes del comienzo de la clase. En la parte inferior se detalla el estado de la reserva y un detalle con el nivel, observación del alumno, horario de la clase y estado.

10- Ingresando a Admin, accederá al menú para toda la administración de la app. Se podrá dar de alta, editar o eliminar profesores, suplentes, clases y reservas.

11- ingresando a Reserva de clases, se apertura un formulario para seleccionar profesor, suplente, nivel, descripción, fecha de inicio / finalización y Estado de la reserva. Además, tiene disponible el botón guardar.

12- Ingresando a crear profesor, por el momento solo permite ingresar en nombre.

13- Próximos pasos, agregar un form para alta de alumnos, login y mejorar las opciones actuales.



