from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

load_dotenv()

st.title("ChatGPT con PandasAI")

# Agregar un campo de entrada de texto para que el usuario ingrese el API Key
api_key = st.text_input("Ingrese su API Key de ChatGPT", type="password")

# Verificar si se proporcionó un API Key
if api_key:
    # Crear una instancia de OpenAI con el API Key proporcionado
    llm = OpenAI(api_token=api_key)
    pandas_ai = PandasAI(llm)

    uploaded_file = st.file_uploader("Cargar archivo Excel para el análisis", type=['xlsx'])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(df.head())

        prompt = st.text_area("Ingrese su consulta o pregunta:")

        if st.button("Generar respuesta"):
            if prompt:
                with st.spinner("Generando respuesta ..."):
                    st.write(pandas_ai.run(df, prompt=prompt))
            else:
                st.write("Por favor, ingrese una consulta o pregunta.")
else:
    st.write("Por favor, ingrese su API Key de ChatGPT para comenzar.")
