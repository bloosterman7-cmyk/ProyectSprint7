import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_ch = st.checkbox('Construir histograma')
if hist_ch:
    st.header('Histograma de kilometraje')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_ch = st.checkbox('Construir gráfico de dispersión')
if scatter_ch:
    st.header('Gráfico de dispersión de precio vs kilometraje')
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
