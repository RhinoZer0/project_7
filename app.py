import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv("datasets/vehicles_us.csv")

st.header("Vehículos")

# hist_button = st.button('Construir histograma')  # crear un botón
# scatter_button = st.button('Construir gráfico de dispersión')
build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write('Histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Gráfica de dispersión para la columna odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# if hist_button:  # al hacer clic en el botón
#     # escribir un mensaje
#     st.write(
#         'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

#     # crear un histograma
#     fig = px.histogram(car_data, x="odometer")

#     # mostrar un gráfico Plotly interactivo
#     st.plotly_chart(fig, use_container_width=True)

# if scatter_button:  # al hacer clic en el botón
#     # escribir un mensaje
#     st.write(
#         'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

#     # crear un histograma
#     fig = px.scatter(car_data, x="odometer", y="price")

#     # mostrar un gráfico Plotly interactivo
#     st.plotly_chart(fig, use_container_width=True)
