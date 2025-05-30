# archivo: registro_niñas.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Crear carpeta para fotos si no existe
os.makedirs("fotos", exist_ok=True)

st.title("Registro de Niñas - Programa de Prevención de Abuso")

# Formulario
with st.form("registro_form"):
    nombre = st.text_input("Nombre")
    apellidos = st.text_input("Apellidos")
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    numero_ci = st.text_input("Número de CI")
    nombres_padres = st.text_area("Nombres de los Padres")
    foto = st.file_uploader("Fotografía", type=["jpg", "jpeg", "png"])

    submit = st.form_submit_button("Registrar")

    if submit:
        if not (nombre and apellidos and numero_ci and nombres_padres and foto):
            st.warning("Por favor completa todos los campos.")
        else:
            # Guardar datos en CSV
            datos = {
                "Nombre": nombre,
                "Apellidos": apellidos,
                "Fecha de Nacimiento": fecha_nacimiento.strftime("%Y-%m-%d"),
                "Número de CI": numero_ci,
                "Nombres de los Padres": nombres_padres,
                "Fotografía": foto.name
            }

            df = pd.DataFrame([datos])
            archivo_csv = "registro_niñas.csv"

            if os.path.exists(archivo_csv):
                df.to_csv(archivo_csv, mode='a', header=False, index=False)
            else:
                df.to_csv(archivo_csv, index=False)

            # Guardar la foto
            with open(os.path.join("fotos", foto.name), "wb") as f:
                f.write(foto.read())

            st.success("Niña registrada exitosamente.")
