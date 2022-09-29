# eCommerce

El proyecto tratara sobre la simulacion de un eCommerce de una tienda de ropa ficticia. No tiene la intencion de llevarse a cabo en la vida real, unicamente
el proyecto fue elegido con fines de aprendizaje.

## Base de datos

El esquema de base de datos, inicialmente, sera estructurado tal cual se ve en el PDF adjunto, sujeto a cambios a medida que escalamos el proyecto.

### DB: Usuarios

El PK sera el id que establece Django por defecto.
Tambien contaran con todos los datos que sean necesarios del cliente.

### DB: Producto

La base de datos Producto tiene como fin principal conocer tanto cada uno de los productos especificos como sus caracteristicas, ya sea para aportarle
informacion al cliente externo como para la toma de decisiones internas.
El campo 'valor' dentro de la base de datos de producto nos derivara a una tabla externa, en la cual podremos conocer tanto su costo de adquisicion como su
precio de venta, reflejando asi el margen de ganancias para la gestion interna de la empresa.

## Registro de usuarios

Para la registracion de usuarios se utiliza la app de terceros Registration Redux del modo que la consigna indica. Para ello fue agregado dentro de Settings

# Aplicaciones

## usuarios

La aplicacion usuarios se encarga de realizar una gestion sobre los mismos, sobreescribiendo el objeto User que viene por defecto con Django para poder
agregarle los datos necesarios.

## productos

La aplicacion productos se encarga de realizar la gestion interna y externa de los productos (tanto del lado del usuario como del administrador). Para ello
se encuentra el proceso de desarrollo las bases de datos necesarias para la realizacion del proyecto.

### Otras aclaraciones

1. El archivo styles.css se encuentra dentro de la carpeta de SCSS ya que, al encontrarme trabajando con Pycharm, la compilacion la realiza de manera
   automatica.