#   Flask: Patio de juegos

## Contenido
~~~
    Proyecto Flask de renderizado de plantillas html, en donde se les pasa 
    datos o argumentos a traves del servidor flask para generar contenido   
    dinamico, que pueden ser modificadas a traves de las rutas y tambien 
    implementando logica python en el motor de plantillas Jinja.  
~~~

     Escribir las siguientes rutas: 

    -  http://127.0.0.1:5000/play ==> Muestra 3 cajas azules
    -  http://127.0.0.1:5000/play/(x) ==> Muestra x cantidad de  cajas azules
    -  http://127.0.0.1:5000/play/(x)/(color) ==> Muestra x cantidad de  cajas 
      segun el color elegido (red, green etc...)

## **Instalacion y configuracion**

#### Instalar un entorno virtual con  pipenv en forma global (omitir si ya está instalado):      
#### Window:
    pip install pipenv

#### Mac:
    pip3 install pipenv



#### Clona el repositorio del proyecto: 


    $ git clone https://github.com/JairoFR/flask_patio_juegos.git  
    $ cd flask_patio_juegos

####  Instala desde Pipfile los paquetes que vienen configurados: 
    $ pipenv install

####  Activa el shell de Pipenv:
    $ pipenv shell

####  Detiene  el ambiente virtual en la terminal:
    $ exit


### Abrir proyecto en un editor de codigo fuente

    1.- Abrir proyecto en visual studio code.
    2.- Ir a Python: select interpreter ctrl+shift+p.
    3.- Seleccionar el ambiente virtual creado con el nombre de la carpeta.
    4.- Abrir nueva terminal y escribir python servidor.py
    5.- Escribir rutas especificadas en Seccion contenido.
