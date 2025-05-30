import streamlit as st
import pandas as pd
import os
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="Registro de Niñas", layout="centered")

# Mostrar el logo
if os.path.exists("logo.png"):
    st.image("logo.png", width=200)

st.title("📝 Registro de Niñas - Programa de Prevención")

# Formulario
with st.form("formulario_registro"):
    nombre = st.text_input("Nombre")
    apellidos = st.text_input("Apellidos")
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    ci = st.text_input("Número de CI")
    nombre_padres = st.text_input("Nombre de los Padres")
    fotografia = st.file_uploader("Fotografía", type=["jpg", "jpeg", "png"])

    submit = st.form_submit_button("Registrar")

    if submit:
        if not (nombre and apellidos and ci and nombre_padres and fotografia):
            st.warning("⚠️ Por favor completa todos los campos.")
        else:
            archivo_csv = "registro_ninas.csv"
            ya_existe = False

            # Verificar CI duplicado
            if os.path.exists(archivo_csv):
                df_existente = pd.read_csv(archivo_csv)
                if ci in df_existente["CI"].astype(str).values:
                    ya_existe = True

            if ya_existe:
                st.error("❌ Ya existe un registro con ese número de CI.")
            else:
                # Guardar foto
                os.makedirs("fotos", exist_ok=True)
                extension = os.path.splitext(fotografia.name)[-1]
                nombre_foto = f"{ci}_{nombre}_{apellidos}{extension}"
                ruta_foto = os.path.join("fotos", nombre_foto)
                with open(ruta_foto, "wb") as f:
                    f.write(fotografia.read())

                # Guardar datos
                registro = {
                    "Nombre": nombre,
                    "Apellidos": apellidos,
                    "Fecha de nacimiento": fecha_nacimiento.strftime('%d/%m/%Y'),
                    "CI": ci,
                    "Padres": nombre_padres,
                    "Foto": ruta_foto,
                    "Fecha de registro": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                }

                df_nuevo = pd.DataFrame([registro])
                if os.path.exists(archivo_csv):
                    df_final = pd.concat([pd.read_csv(archivo_csv), df_nuevo], ignore_index=True)
                else:
                    df_final = df_nuevo

                df_final.to_csv(archivo_csv, index=False)
                st.success("✅ Registro guardado correctamente.")
