# Proyecto de Análisis de Datos de Vehículos

Este proyecto consiste en una aplicación web desarrollada con **Streamlit** para explorar y visualizar datos de vehículos. Los datos provienen de un conjunto de datos sobre vehículos en Estados Unidos, y la aplicación permite crear visualizaciones interactivas usando gráficos generados con **Plotly**.

## Descripción de la Aplicación Web

La aplicación web proporciona una interfaz interactiva donde los usuarios pueden:

1. **Ver un histograma** de la distribución de los valores del odómetro de los vehículos.
2. **Ver un gráfico de dispersión** que muestra la relación entre el año del modelo de los vehículos y su precio.

La aplicación permite explorar los datos de manera sencilla y rápida, ayudando a identificar patrones y distribuciones en los datos de vehículos.

## Funcionalidades

- **Histograma de Odómetro**: Permite ver la distribución de los valores del odómetro para el conjunto de datos de vehículos.
- **Gráfico de Dispersión**: Muestra la relación entre el año del modelo y el precio de los vehículos.

## Requisitos

Para ejecutar esta aplicación, necesitas instalar las siguientes librerías:

- `streamlit`
- `pandas`
- `plotly.express`

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt

#  Clona este repositorio en tu máquina local
git clone <URL_DEL_REPOSITORIO>

# Accede al directorio del proyecto
cd <NOMBRE_DEL_PROYECTO>

# Crea y activa un entorno virtual
python -m venv venv
venv\Scripts\activate  # En Windows
source venv/bin/activate  # En Mac/Linux

# Instala las dependencias necesarias
pip install -r requirements.txt

# Corre la aplicación con el siguiente comando
streamlit run app.py

Render URL: https://proyecto-sprint-7-analisis-de-vehiculos.onrender.com