import streamlit as st
import requests
from datetime import datetime

# Configuration
API_URL = "http://localhost:3001"


def get_users():
    """Fetch all users from the API"""
    try:
        response = requests.get(f"{API_URL}/usuarios")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error al obtener usuarios: {response.text}")
            return []
    except Exception as e:
        st.error(f"Error de conexión: {str(e)}")
        return []


def create_user(user_data):
    """Create a new user via API"""
    try:
        response = requests.post(f"{API_URL}/usuarios", json=user_data)
        if response.status_code == 200:
            return True, "Usuario creado exitosamente"
        else:
            return False, f"Error al crear usuario: {response.text}"
    except Exception as e:
        return False, f"Error de conexión: {str(e)}"


# Page configuration
st.set_page_config(page_title="Gestión de Usuarios", page_icon="👥")

# Title
st.title("Gestión de Usuarios")

# Tabs for different operations
tab1, tab2 = st.tabs(["Listar Usuarios", "Crear Usuario"])

# List Users Tab
with tab1:
    st.header("Lista de Usuarios")
    users = get_users()

    if users:
        # Convert to DataFrame for better display
        import pandas as pd

        df = pd.DataFrame(
            users,
            columns=[
                "ID",
                "Nombre",
                "Apellido",
                "Usuario",
                "Fecha Registro",
                "Email",
                "Celular",
                "Ubicación",
            ],
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay usuarios registrados")

# Create User Tab
with tab2:
    st.header("Crear Nuevo Usuario")

    with st.form("create_user_form"):
        col1, col2 = st.columns(2)

        with col1:
            consec_user = st.text_input("ID Usuario", max_chars=5)
            nombre = st.text_input("Nombre", max_chars=25)
            apellido = st.text_input("Apellido", max_chars=25)
            usuario = st.text_input("Usuario", max_chars=6)

        with col2:
            email = st.text_input("Email", max_chars=50)
            celular = st.text_input("Celular", max_chars=16)
            cod_ubica = st.text_input("Código Ubicación", max_chars=4)
            fecha_registro = st.date_input("Fecha de Registro", datetime.now())

        submitted = st.form_submit_button("Crear Usuario")

        if submitted:
            if not all(
                [
                    consec_user,
                    nombre,
                    apellido,
                    usuario,
                    email,
                    celular,
                    cod_ubica,
                ]  # noqa: E501
            ):
                st.error("Por favor complete todos los campos")
            else:
                user_data = {
                    "consecUser": consec_user,
                    "nombre": nombre,
                    "apellido": apellido,
                    "usuario": usuario,
                    "fechaRegistro": fecha_registro.strftime("%Y-%m-%d"),
                    "email": email,
                    "celular": celular,
                    "codUbica": cod_ubica,
                }

                success, message = create_user(user_data)
                if success:
                    st.success(message)
                    st.rerun()  # Refresh page to show new user
                else:
                    st.error(message)
