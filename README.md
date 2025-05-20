# Sistema de Recomendación de artistas musicales con Apache Spark y Angular

Este proyecto implementa un sistema de recomendación de artistas musicales utilizando Apache Spark y el algoritmo ALS (Alternating Least Squares). Cuenta con un frontend en Angular y un backend en FastAPI.

# Integrantes

- Camacho Palma Anthony
- Diaz Barrios Angelica Maria
- Jimenez Vargas Jose Mario
- Porras Briones Saymon
- Ramirez Viales Amanda Karina


## Dataset Utilizado

Se utilizó el dataset [hetrec2011-lastfm-2k](http://ir.ii.uam.es/hetrec2011), creado por Ignacio Fernández-Tobías, Iván Cantador y Alejandro Bellogín. Archivos usados:

- `user_artists.dat`: contiene tripletas (userID, artistID, weight)
- `artists.dat`: contiene información de artistas (id, name, url, pictureURL)

Estos archivos fueron convertidos a `.parquet` para su procesamiento con Apache Spark.

## Requisitos

### Backend
- Python 3.10
- Apache Spark 3.5.5
- Java 11 (Adoptium)
- FastAPI
- PySpark
- Pandas
- PyArrow

### Frontend
- Node.js
- TypeScript
- Angular CLI 16
- Angular Material

### Variables de entorno
- `HADOOP_HOME=C:/winutils` (en Windows)
- `JAVA_HOME` apuntando a Java 11
- `PYSPARK_PYTHON` usando el Python del entorno virtual
- `SPARK_HOME` apuntando a la carpeta descomprimida de su descarga 

## Estructura del Proyecto

```
Prototipo-BD2/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py         # Rutas del backend API
│   │   ├── data/                 # Archivos Parquet procesados
│   │   ├── utils/
│   │   │   └── spark.py          # Configuración de SparkSession
│   │   ├── main.py               # Punto de arranque de FastAPI
│   │   ├── recommender.py        # Lógica de recomendaciones con ALS
│   │   └── __init__.py           # Vacío, pero necesario para que Python lo reconozca como paquete
│   └── convert_to_parquet.py     # Script para transformar .dat a .parquet
├── frontend/
│   └── angular-app/
│       └── src/
│           ├── app/
│           │   ├── music/
│           │   │   ├── pages/recommendations/
│           │   │   │   ├── recommendations.component.html
│           │   │   │   ├── recommendations.component.ts
│           │   │   │   └── recommendations.component.css
│           │   │   └── services/recommendation.service.ts
│           └── assets/default-music.png
├── venv310/                      # Entorno virtual (añadir a .gitignore)
├── requirements.txt              # Dependencias del backend
```

## Instalación y Ejecución del Proyecto

Siga estos pasos para clonar, instalar y ejecutar el prototipo:

### 1. Clonar el repositorio

```bash
git clone https://github.com/AngelicaDiazB14/Prototipo-BD2.git
cd Prototipo-BD2
```

### 2. Backend (FastAPI + Spark)

Abra una terminal en la raíz del proyecto y ejecute lo siguiente:

```bash
# Crear y activar entorno virtual (si no está presente)
python -m venv venv310
.env310\Scriptsctivate # En Linux/Mac: source venv310/bin/activate

# Cuando active el entorno virtual ejecute:

# Para instalar depedencias, librerías...
pip install -r requirements.txt

# Ejecutar servidor FastAPI
uvicorn app.main:app --reload --app-dir backend/app
```

### 3. Frontend (Angular)

```bash
cd frontend/angular-app

# Instalar dependencias
npm install

# Ejecutar Angular
ng serve
```

### Notas adicionales

- Asegúrese de tener configurado `JAVA_HOME` y `HADOOP_HOME` correctamente.

## Cómo Funciona la Recomendación

Apache Spark:
- Carga datos en formato `.parquet`
- Entrena un modelo ALS usando `userID`, `artistID`, `weight`
- Excluye automáticamente artistas ya escuchados por el usuario
- Calcula un puntaje estimado de afinidad y genera recomendaciones

## Licencia del Dataset

Fuente: http://www.last.fm y http://ir.ii.uam.es/hetrec2011  
Autores: Ignacio Fernández-Tobías, Iván Cantador, Alejandro Bellogín  
Uso permitido: no comercial
