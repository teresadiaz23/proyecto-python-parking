# Proyecto Parking en Python en aplicación web con Flask
## Información sobre el proyecto
El proyecto consiste en el uso de un parking por parte de clientes normales y clientes abonados, y de la gestión del mismo por parte de un administrador.
1. En la barra del menú hay 3 zonas de acceso, una para un cliente normal, otra para un cliente abonado y otra para el administrador.
2. Se guardan los datos de los clientes abonados, los tickets, los abonos, las plazas y un parking en una base de datos sqlite usando SQLAlchemy.
3. Para acceder a la zona de administración hay que introducir la contraseña 1234.
4. Hay creados de inicio en la base de datos: 4 clientes abonados y por consiguiente 4 abonos, 3 vehículos, 60 plazas y 3 tickets de prueba.
5. Para probar las opciones de un abonado se pueden usar los datos de uno de ellos:
    - dni = 1234
    - pin = 111
    - matricula = 1234BBB
    - id plaza = 3
6. Un cliente normal puede depositar su vehículo, retirarlo o sacarse un abono.
7. Un cliente abonado puede depositar o retirar su vehículo, ver su abono, ver sus datos personales, modificar alguno de sus datos personales, renovar su abono o borrar su abono.
8. El administrador puede ver el estado de las plazas del parking, ver la facturación de los coches depositados de los clientes normales, ver los abonos que hay y la facturación de los mismo. También puede ver los abonos que caducan en un mes concreto y los que van a caducar en los próximos 10 días.
9. Los repositorios hacen consultas a la base de datos para obtener los datos de las clases modelo, los servicios envuelven a los repositorios y los controladores llaman a los métodos de los servicios. En el fichero app.py se encuentran los métodos controladores, siendo los métodos que corresponden a las diferentes rutas de la aplicación.
10. Para ejecutarlo:
    - Abrir la consola y ejecutar el siguiente comando: *pip install -r requirements.txt* para instalar las librerias necesarias.
    - Luego ejecutar *python manage.py runserver* para iniciar la aplicación y entrar en localhost:5000.
11. Para ver las tablas y los datos guardados en la base de datos, abrir el archivo dbase.bd con sqlite browser o alguno similar.
12. Para borrar las tablas se ejecuta *python manage.py drop_tables*, y para crearla y guardar datos iniciales se ejecuta *python manage.py add_data_tables*.