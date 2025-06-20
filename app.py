import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de vehículos en EE.UU.")  # encabezado de la aplicación
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
# crear un histograma
    fig = px.histogram(car_data, x="odometer")
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
if st.checkbox('Mostrar tabla de datos'):
    st.write(car_data.head())

# Filtro: tipo de vehículo
vehicle_type = st.selectbox(
    'Selecciona tipo de vehículo', car_data['type'].dropna().unique())
filtered_data = car_data[car_data['type'] == vehicle_type]

# Botón 1: Histograma de precios
if st.button('Mostrar histograma de precios'):
    st.write(f'Distribución de precios para vehículos tipo "{vehicle_type}":')
    fig_hist = px.histogram(filtered_data, x='price',
                            nbins=30, title='Histograma de Precios')
    st.plotly_chart(fig_hist)

# Botón 2: Gráfico de dispersión (precio vs. año)
if st.button('Mostrar dispersión precio vs. año'):
    st.write(
        f'Relación entre el año del modelo y el precio para tipo "{vehicle_type}":')
    fig_scatter = px.scatter(filtered_data, x='model_year', y='price',
                             color='condition', title='Dispersión: Precio vs. Año del Modelo')
    st.plotly_chart(fig_scatter)
