
import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Población mundial", layout="wide")


st.title("Análisis de población mundial")
st.write("Los 10 países más poblados")


archivo = st.file_uploader("Selecciona el archivo CSV", type="csv")


if archivo :

    datos = pd.read_csv(archivo)

   
    top10 = datos.sort_values(
        "2022 Population",
        ascending=False
    ).head(10)

    
    paises = top10["Country/Territory"].to_numpy()

    poblacion_2015 = top10["2015 Population"].to_numpy()
    poblacion_2020 = top10["2020 Population"].to_numpy()
    poblacion_2022 = top10["2022 Population"].to_numpy()

    
    total = np.sum(poblacion_2022)
    promedio = np.mean(poblacion_2022)
    mediana = np.median(poblacion_2022)
    minimo = np.min(poblacion_2022)
    maximo = np.max(poblacion_2022)

    
    st.subheader("Estadísticas de población (2022)")

    col1, col2, col3= st.columns(3)

    col1.metric("Población total", f"{total / 1000000:,.2f} millones")
    col2.metric("Promedio", f"{promedio / 1000000:,.2f} millones")
    col3.metric("Mediana", f"{mediana / 1000000:,.2f} millones")

    
    col4, col5, col6 = st.columns(3) 

    col4.metric("Población mínima", f"{minimo / 1000000:,.2f} millones")
    col5.metric("Población máxima", f"{maximo / 1000000:,.2f} millones")

    
    st.subheader("Comparación de población por país")

   
    grafico = top10.set_index("Country/Territory")[[
        "2015 Population",
        "2020 Population",
        "2022 Population"
    ]] / 1000000

    st.bar_chart(grafico)

  
    st.subheader("Datos de los 10 países")

    st.dataframe(top10[[
        "Country/Territory",
        "2015 Population",
        "2020 Population",
        "2022 Population"
    ]])

else:
    st.info("Primero debes cargar el archivo CSV.")

