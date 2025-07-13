import pandas as pd
import plotly
import plotly.graph_objects as go 
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write ('creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribucion del odometro')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión entre el odómetro y el precio')
    fig_scatter = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'))
    fig_scatter.update_layout(title='Relación entre Odómetro y Precio',
                              xaxis_title='Odómetro (millas)',
                              yaxis_title='Precio (USD)')

    st.plotly_chart(fig_scatter, use_container_width=True)