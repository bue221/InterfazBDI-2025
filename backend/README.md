# Backend Python con Flask y Oracle

Este es el backend de la aplicación, desarrollado en Python usando Flask y Oracle Database.

## Requisitos

- Python 3.8 o superior
- Oracle Database 11g
- Cliente Oracle (Oracle Instant Client)

## Instalación

1. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar Oracle Instant Client:
   - Descargar Oracle Instant Client desde la página oficial de Oracle
   - Configurar las variables de entorno según tu sistema operativo
   - En macOS/Linux, agregar al PATH:
     ```bash
     export LD_LIBRARY_PATH=/path/to/instantclient:$LD_LIBRARY_PATH
     ```

## Configuración

1. Asegúrate de que Oracle Database esté corriendo y accesible
2. Verifica las credenciales en `app.py`:
   ```python
   db_config = {
       'user': 'SYS',
       'password': 'MiClave123',
       'dsn': 'localhost:1521/ORCLCDB',
       'privilege': oracledb.SYSDBA
   }
   ```

## Ejecución

1. Activar el entorno virtual (si no está activado):
```bash
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Iniciar el servidor:
```bash
python app.py
```

El servidor estará disponible en `http://localhost:3001`

## Endpoints

- `GET /usuarios`: Obtiene todos los usuarios
- `GET /ubicaciones`: Obtiene todas las ubicaciones
- `POST /usuarios`: Crea un nuevo usuario
- `GET /setup`: Ejecuta las migraciones y datos de prueba

## Estructura del Proyecto

```
backend/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
├── db/                 # Scripts SQL
│   ├── migrations.sql  # Migraciones
│   └── dataTest.sql    # Datos de prueba
└── README.md          # Este archivo
``` 