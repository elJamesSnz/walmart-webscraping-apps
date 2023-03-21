# walmart-webscraping-apps

# 1. Librerías usadas

## Lista de las librerías utilizadas en el proyecto.
- Selenium
- webdriver-manager

# 2. Pasos para instalación
Instrucciones para instalar proyecto (VS Code)

## Clonar proyecto
Usar Github Desktop

### Comandos ejecución

- python3 -m venv venv
- ./venv/Scripts/activate
- pip install selenium
- pip install webdriver-manager
- py main.py


# 3. Posibles incidencias
Lista de posibles incidencias.

## 3.1 Bloqueos
Walmart no es amigable para desarrolladores que intentan obtener información de su página a través de web scraping. Tienen desafíos que buscan prevenir el uso de bots / webdrivers

## 3.2 Complejidades
La terminal de VS Code no encuentra un intérpte de Python y/o ambiente de desarrollo correcto
CTRL + SHIFT + P -> Seleccionar intérprete -> seleccionar recomendado (./venv/)
Para el segundo ejercicio, desde la página a la que se accede en Walmart (listado de productos por categoría seleccionada) se presenta un bloqueo adicional que no permite recuperar los productos desde el contenedor

## 3.3 Retrasos
El aplicativo puede tardar en recuperar la información (valida si hay desafío anti bot que consiste en hacer click en la página y hacer hold de ese click por cierta cantidad de segundos).
Se puede ver en consola el mensaje "Click & hold verificado" cuando tuvo que cumplir con el desafío
Se puede ver en consola el mensaje "no hay click and hold" cuando no tuvo que cumplir con el desafío


# 4 Uso
Instrucciones para su uso.

## 4.1 PRIMER EJERCICIO. 

### Comandos
- ./venv/Scripts/activate
-  py main.py

### Salida

Archivo JSON en local llamado "categorias.json"

NOTA. Para ambos casos, la petición tarda por la posible verificación click & hold.

## 4.2 SEGUNDO EJERCICIO.

### Comandos
- ./venv/Scripts/activate
-  py main.py

Indicar URL (debe ser alguna subcategoría del URL https://super.walmart.com.mx/all-departments)

![image](https://user-images.githubusercontent.com/72090281/226672241-3d6dfc1a-2e3c-4cf7-8bb8-38d45a3958f1.png)


Salida
Archivo JSON en local llamado "productos.json"

# Autores
Angel Sánchez


