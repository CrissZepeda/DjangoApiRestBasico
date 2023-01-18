## DJango ApiRest básico

###Instalación
Una vez clonado el proyecto, se debe instalar la base de datos, en este caso mysql.

#### Configuracion del proyecto

- Crear tabla en mysql "django_reservas"
- Abrir la siguiente en el proyecto ruta evaluacion4 > setting.py
- Modificar la linea 86 con el usuario de mysql
- Modificar la linea 87 con el password de mysql
- Guardar configuración.

#### Migración

En la raiz del proyecto se deben ejecutar los siguientes comandos.

- **"python manage.py makemigrations evaluacion4"**, esto creara una carpeta con las tablas y campos para migrar a mysql.
- **"python manage.py migrate"**, con este comando se realizaran las migraciónes a la base de datos.

#### Ejecutar

Una vez realizada la configuración, creada la migracion y aplicada, simplemente se debe ejecutar la aplicacion con el siguiente comando:
**"python manage.py runserver"**
