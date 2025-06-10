# Frontend Streamlit para Gestión de Usuarios

Este es un frontend alternativo desarrollado con Streamlit para la gestión de usuarios.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Asegúrate de que el backend esté corriendo en http://localhost:3001

2. Inicia la aplicación Streamlit:
```bash
streamlit run app.py
```

3. Abre tu navegador en http://localhost:8501

## Características

- Lista de usuarios en formato tabla
- Formulario para crear nuevos usuarios
- Validación de campos
- Interfaz intuitiva y responsive 