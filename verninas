import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

st.set_page_config(page_title="Registro de Niñas", layout="centered")

st.image("logo.png", width=150)
st.title("Formulario de Registro - Prevención")

# Autenticación con Google Sheets
alcance = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credenciales = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", alcance)
cliente = gspread.authorize(credenciales)
hoja = cliente.open("RegistroNinas").sheet1

with st.form("registro"):
    nombre = st.text_input("Nombre")
    apellidos = st.text_input("Apellidos")
    fecha_nac = st.date_input("Fecha de Nacimiento", min_value=date(2000, 1, 1))
    ci = st.text_input("Número de C.I.")
    padres = st.text_input("Padres o Tutores")
    enviar = st.form_submit_button("Guardar")

if enviar:
    hoja.append_row([nombre, apellidos, str(fecha_nac), ci, padres])
    st.success("Registro guardado correctamente ✅")

if st.checkbox("Ver registros"):
    registros = hoja.get_all_records()
    st.dataframe(pd.DataFrame(registros))
