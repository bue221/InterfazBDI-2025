import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import re

# Configuration
API_URL = "http://localhost:3001"


def validate_email(email):
    """Validate email format using regex"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


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


def get_locations():
    """Fetch all locations from the API"""
    try:
        response = requests.get(f"{API_URL}/ubicaciones")
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            st.error(f"Error al obtener ubicaciones: {response.text}")
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

    # Obtener ubicaciones
    locations = get_locations()
    location_dict = (
        {f"{loc[1]} ({loc[0]})": loc[0] for loc in locations}
        if locations
        else {}  # noqa: E501
    )

    with st.form("create_user_form"):
        col1, col2 = st.columns(2)

        with col1:
            consec_user = st.text_input(
                "ID Usuario", max_chars=5, key="consec_user"
            )  # noqa: E501
            nombre = st.text_input("Nombre", max_chars=25, key="nombre")
            apellido = st.text_input("Apellido", max_chars=25, key="apellido")
            usuario = st.text_input("Usuario", max_chars=6, key="usuario")

        with col2:
            email = st.text_input("Email", max_chars=50, key="email")
            celular = st.text_input("Celular", max_chars=16, key="celular")
            selected_location = st.selectbox(
                "Ubicación",
                options=list(location_dict.keys()),
                format_func=lambda x: x,
                key="selected_location",
            )
            fecha_registro = st.date_input(
                "Fecha de Registro", datetime.now(), key="fecha_registro"
            )

        submitted = st.form_submit_button("Crear Usuario")

        if submitted:
            if not all(
                [consec_user, nombre, apellido, usuario, email, celular]
            ):  # noqa: E501
                st.error("Por favor complete todos los campos")
            elif not validate_email(email):
                st.error("Por favor ingrese un email válido")
            else:
                user_data = {
                    "consecUser": consec_user,
                    "nombre": nombre,
                    "apellido": apellido,
                    "usuario": usuario,
                    "fechaRegistro": fecha_registro.strftime("%Y-%m-%d"),
                    "email": email,
                    "celular": celular,
                    "codUbica": location_dict[selected_location],
                }

                success, message = create_user(user_data)
                if success:
                    st.success(message)
                    # Use rerun to refresh the page instead of modifying session state  # noqa: E501
                    st.rerun()
                else:
                    st.error(message)
