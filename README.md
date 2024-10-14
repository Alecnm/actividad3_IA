# Proyecto de Predicción de Espera en Transporte Masivo

## Descripción

Este proyecto aplica un modelo de **aprendizaje supervisado** para predecir si un pasajero experimentará una espera larga en una ruta de transporte masivo. Utilizando datos históricos de factores como el número de pasajeros, condiciones climáticas, y nivel de congestión, el modelo aprende patrones que pueden usarse para hacer predicciones futuras.

El objetivo de este proyecto es ayudar a optimizar la operación del sistema de transporte masivo, permitiendo una mejor planificación y asignación de recursos para reducir los tiempos de espera de los pasajeros.

## Dataset

El dataset utilizado contiene información simulada sobre varias rutas de transporte, incluyendo:
- **Rutas**: Identificador de la ruta (ej. A, B, C).
- **Pasajeros**: Número promedio de pasajeros por día.
- **Tiempo de viaje**: Duración promedio del viaje en minutos.
- **Clima**: Condiciones climáticas (soleado, nublado, lluvioso).
- **Congestión**: Nivel de congestión (alta, media, baja).
- **Espera larga**: Variable binaria (0 o 1) que indica si un pasajero experimentó una espera larga.

El archivo con el dataset simulado está ubicado en la carpeta `data/transporte.csv`.

## Instalación y configuración

Para ejecutar este proyecto, asegúrate de tener **Python 3.x** instalado y sigue los siguientes pasos:

1. Clona este repositorio:
   ```bash 
   git clone https://github.com/usuario/proyecto_transporte_masivo.git
2. Navega a la carpeta del proyecto:
   ```bash 
    cd proyecto_transporte_masivo
3. Instala las dependencias necesarias:
   ```bash 
    pip install -r requirements.txt

## Uso del Proyecto
Este proyecto está organizado de la siguiente manera:

- src/main.py: Archivo principal que ejecuta el flujo del proyecto. Carga los datos, entrena el modelo, y muestra la precisión obtenida.
- src/modelo.py: Contiene las funciones para entrenar y evaluar el modelo de aprendizaje automático (un árbol de decisión en este caso).
- data/transporte.csv: Dataset simulado que contiene información sobre las rutas de transporte y los factores que afectan los tiempos de espera.

## Ejecutar el proyecto
1. Asegúrate de que los datos estén en el archivo data/transporte.csv.
2. Navega a la carpeta del proyecto:
   ```bash 
    python src/main.py
3. El programa cargará los datos, entrenará el modelo y mostrará en pantalla la precisión del modelo en predecir si habrá una espera larga en una ruta determinada.

### Ejemplo de salida

- Al ejecutar el proyecto, verás un resultado como el siguiente:
    ```txt
    Precisión del modelo: 0.83

### Estructura del proyecto
    proyecto_transporte_masivo/
    │
    ├── data/
    │   └── transporte.csv        # Archivo de datos (dataset simulado)
    │
    ├── src/
    │   ├── main.py               # Archivo principal que ejecuta el modelo
    │   ├── modelo.py             # Archivo con la lógica del modelo de aprendizaje supervisado
    │
    ├── README.md                 # Este archivo, descripción del proyecto
    ├── requirements.txt          # Lista de dependencias necesarias
    └── .gitignore                # Archivos ignorados por Git
