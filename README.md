## Proyecto Final - Pilates Center

### Alumnos: Mancino Melina, Sandoval Valentín

Se crea un proyecto basado en un centro de Pilates, donde los usuarios podrán ver las reservas de clases, crearlas o registrar alumnos.

Pasos implementados:

1- Creamos el proyecto: 
   python3 -m django startproject "PilatesCenter"

2- Creamos la aplicación 
   python manage.py startapp "reserves"   

3- Creamos un archivo urls.py dentro de la carpeta de la app

4- Configuramos el proyecto, agregando la aplicación en seetings y configurando las urls del proyecto para que se conecten con las urls generales

5- Comenzamos a crear la aplicación.
a- Se crea la carpeta static que contiene de forma local los archivos ccs que utilizaremos en nuestro diseño.
b- Creamos los 4 modelos de nuestra app: Profesor, Suplente, Clase y Estado. Realizamos la migración para que impacte en la app, mediante python manage.py makemigrations seguido de python manage.py migrate
c- Creamos las funciones en las vistas
d- Creamos un archivo de forms donde importamos los modelos y los creamos 
e- Configuramos las urls para que sean vinculadas a los templates
f- Configuramos los templates por cada clase

6- Generamos un usuario "Admin" pass "123456" con python manage.py createsuperuser --username=admin --email=aa@com.ar

7- Accedemos a la app corriendo el servidor mediante python manage.py runserver http://127.0.0.1:8000/ donde se encuentra el home de la web.

8- Para ingresar al menú de opciones ingresamos un la url http://127.0.0.1:8000/reserves/ en la misma, se visualiza un mensaje de bienvenida y los accesos a Reservas, Admin, Crear Reservas y Crear Profesor.

9- Ingresando a Reservas, se apertura una tarjeta que muestre el resumen de los datos registrados. Ej.: en la parte superior se encuentra el nombre del profesor y el suplente, en el medio el nivel de la clase reservada, abajo una observación particular del alumno para que el profesor considere antes del comienzo de la clase. En la parte inferior se detalla el estado de la reserva y un detalle con el nivel, observación del alumno, horario de la clase y estado.

10- Ingresando a Admin, accederá al menú para toda la administración de la aplicación. Se podrá dar de alta, editar o eliminar profesores, suplentes, clases y reservas.

11- ingresando a Reserva de clases, se apertura un formulario para seleccionar profesor, suplente, nivel, descripción, fecha de inicio / finalización y Estado de la reserva. Además, tiene disponible el botón guardar.

12- Ingresando a crear profesor, por el momento solo permite ingresar en nombre.

13- Se genera la opción para crear un login para cada usuario registrado en el centro.

14- Cada usuario podrá ingresar a la web y visualizar las clases disponibles con el detalle de los niveles y profesores.

15- Desde las vistas se limitan los accesos a las funciones con "@login_required" y en clases basadas en vistas "LoginRequiredMixin" para que solo los usuarios habilitados desde el admin puedan generar los cambios correspondientes.

16- Se agrega la opción para generar un avatar por usuario o cambiarlo. Para que sea posible instalamos python -m pip install Pillow

17- Agregamos la opción de búsqueda, desde el homepage http://127.0.0.1:8000/ para que pueda accederse al resto de la web.

18- Creamos un usuario de analista con permisos especiales de modificación, pero con restricción de eliminación de usuarios, profesores o clases.
Permisos analista:
user: Analista_PILATES
pass: PilatesCenter2024

19- Se realizan ajustes en el diseño de los formularios con html para realizar mejoras estéticas.

20- Creación de la sección "About" para disponibilidad en la homepage y cada usuario pueda acceder.

Conclusiones:

Este proyecto ha permitido desarrollar una página web completa y funcional para un centro de Pilates. La aplicación cumple con los requisitos iniciales y ofrece funcionalidades adicionales que pueden ser ampliadas en el futuro.



