import streamlit as st
import os

# Configuración del directorio de subida
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Función para guardar archivos
def save_uploaded_file(uploaded_file):
    with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    return st.success(f"Archivo {uploaded_file.name} guardado en {UPLOAD_FOLDER}")

# Título de la aplicación
st.title('Aplicación para Subir y Descargar Archivos')

# Formulario para subir archivos
uploaded_file = st.file_uploader("Carga tu archivo aquí:", type=['pdf', 'csv', 'txt', 'png'])
if uploaded_file is not None:
    save_uploaded_file(uploaded_file)

# Mostrar lista de archivos subidos con enlaces de descarga
st.subheader('Archivos Subidos')
uploaded_files = os.listdir(UPLOAD_FOLDER)
for file in uploaded_files:
    file_path = os.path.join(UPLOAD_FOLDER, file)
    with open(file_path, 'rb') as f:
        file_data = f.read()
        st.download_button(label=f"Descargar {file}", data=file_data, file_name=file)