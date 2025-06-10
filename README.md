# InterfazBDI-2025

Este proyecto consiste en una interfaz web para interactuar con una base de datos Oracle, desarrollada con Streamlit en el frontend y Node.js en el backend.

## Requisitos Previos

### Sistema Operativo
- macOS (recomendado) o Linux
- Node.js (versión 18 o superior)
- pnpm (versión 10.11.0 o superior)
- Python 3.8 o superior
- Oracle Database 19c o superior
- Oracle Instant Client

### Instalación de Oracle Instant Client

#### macOS (usando Homebrew)
```bash
brew install instantclient-basic
```

#### Linux (Ubuntu/Debian)
```bash
# Descargar Oracle Instant Client
wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basic-linuxx64.zip

# Instalar dependencias
sudo apt-get install libaio1

# Descomprimir y configurar
unzip instantclient-basic-linuxx64.zip
sudo mv instantclient_* /opt/oracle/instantclient
sudo ln -s /opt/oracle/instantclient/libclntsh.so.* /opt/oracle/instantclient/libclntsh.so

# Configurar variables de entorno
echo 'export LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export PATH=/opt/oracle/instantclient:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Estructura del Proyecto

```
.
├── streamlit-frontend/  # Aplicación Streamlit
├── backend/            # Servidor Node.js
└── InterfazBDI-2025.pdf # Documentación del proyecto
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd InterfazBDI-2025
```

### 2. Configurar el Backend

```bash
cd backend
pnpm install
```

Configura las variables de entorno necesarias para la conexión a Oracle:
- Crea un archivo `.env` en el directorio `backend/` con las siguientes variables:
  ```
  ORACLE_USER=tu_usuario
  ORACLE_PASSWORD=tu_contraseña
  ORACLE_CONNECTION_STRING=tu_connection_string
  PORT=3000
  ```

Para obtener el connection string de Oracle:
1. Abre SQL*Plus o SQL Developer
2. Ejecuta: `SELECT sys_context('userenv', 'db_name') FROM dual;`
3. El formato del connection string será: `localhost:1521/XE` (para Express Edition) o `hostname:puerto/service_name`

### 3. Configurar el Frontend (Streamlit)

```bash
cd streamlit-frontend
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

### Backend

```bash
cd backend
pnpm start
```

El servidor backend se ejecutará en `http://localhost:3000`

### Frontend (Streamlit)

```bash
cd streamlit-frontend
streamlit run app.py
```

La aplicación frontend estará disponible en `http://localhost:8501`

## Scripts Disponibles

### Backend
- `pnpm start`: Inicia el servidor backend
- `pnpm dev`: Inicia el servidor en modo desarrollo con hot-reload
- `pnpm test`: Ejecuta las pruebas unitarias

### Frontend (Streamlit)
- `streamlit run app.py`: Inicia la aplicación Streamlit
- `streamlit run app.py --server.port 8502`: Inicia en un puerto específico

## Tecnologías Utilizadas

### Frontend
- Streamlit
- Python
- Pandas
- Plotly

### Backend
- Node.js
- Express
- OracleDB
- CORS

## Desarrollo

1. Asegúrate de tener todas las dependencias instaladas
2. Verifica que Oracle Instant Client esté correctamente configurado
3. Inicia el servidor backend
4. En otra terminal, inicia el servidor frontend de Streamlit
5. Los cambios en el frontend se reflejarán automáticamente

## Solución de Problemas Comunes

### Error de conexión a Oracle
1. Verifica que Oracle Instant Client esté instalado correctamente
2. Confirma que las variables de entorno estén configuradas
3. Verifica que el servicio de Oracle esté corriendo
4. Comprueba que el connection string sea correcto

### Error en Streamlit
1. Asegúrate de estar en el entorno virtual correcto
2. Verifica que todas las dependencias estén instaladas
3. Comprueba que el puerto 8501 esté disponible

## Contribución

1. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
2. Commit tus cambios (`git commit -m 'feat: add some amazing feature'`)
3. Push a la rama (`git push origin feature/AmazingFeature`)
4. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia ISC. 