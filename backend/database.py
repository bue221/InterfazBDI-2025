import oracledb
import time

# Indica dónde están las librerías nativas de tu Oracle XE
oracledb.init_oracle_client(
    lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin"
)

# Configura tu usuario, contraseña y DSN
db_config = {
    "user": "BD81",
    "password": "BD81",
    "dsn": "127.0.0.1:1521/xe"  # Usa 'xe' (según lsnrctl status)
}

def test_connection():
    print("Iniciando prueba de conexión...")
    start = time.time()
    try:
        conn = oracledb.connect(**db_config)
        elapsed = time.time() - start
        print(f"✅ Conexión exitosa en {elapsed:.2f} segundos.")
        conn.close()
    except oracledb.Error as err:
        elapsed = time.time() - start
        print(f"❌ Error de conexión tras {elapsed:.2f} segundos.")
        print("Detalle del error:", repr(err))

if __name__ == "__main__":
    test_connection()
