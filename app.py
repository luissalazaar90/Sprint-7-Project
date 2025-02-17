import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV en un DataFrame
df = pd.read_csv("C:/Users/luiss/OneDrive - Universidad Tecmilenio/Desktop/Proyecto Sprint 7/Sprint-7-Project/vehicles_us.csv")

# Encabezado de la aplicación
st.header("Análisis de Datos de Vehículos")

# Botón para mostrar Histograma
if st.button("Mostrar Histograma de Odómetro"):
    st.write("Histograma del Odómetro")
    fig_hist = px.histogram(df, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig_hist)

# Botón para mostrar Gráfico de Dispersión
if st.button("Mostrar Gráfico de Dispersión entre Año y Precio"):
    st.write("Gráfico de Dispersión: Año vs Precio")
    fig_scatter = px.scatter(df, x="model_year", y="price", title="Relación entre Año del Modelo y Precio")
    st.plotly_chart(fig_scatter)



