from flask import Flask, jsonify, request
from flask_cors import CORS
import oracledb

app = Flask(__name__)
CORS(app)

# Indica dónde están las librerías nativas de tu Oracle XE
oracledb.init_oracle_client(
    lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin"
)

# Database configuration
db_config = {
    "user": "BD81",
    "password": "BD81",
    "dsn": "localhost:1521/XEXDB",
    # "privilege": oracledb.SYSDBA,
}


def get_db_connection():
    return oracledb.connect(**db_config)


@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    connection = None
    try:
        connection = get_db_connection()
        print(connection)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Usuario")
        columns = [col[0] for col in cursor.description]
        usuarios = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            connection.close()


@app.route("/ubicaciones", methods=["GET"])
def get_ubicaciones():
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT codUbica, nomUbica, tipoUbica 
            FROM Ubicacion 
            ORDER BY nomUbica
        """
        )
        columns = [col[0] for col in cursor.description]
        ubicaciones = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(ubicaciones)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            connection.close()


@app.route("/usuarios", methods=["POST"])
def create_usuario():
    connection = None
    try:
        data = request.json
        connection = get_db_connection()
        cursor = connection.cursor()

        # Verify location exists
        cursor.execute(
            "SELECT COUNT(*) FROM Ubicacion WHERE codUbica = :1",
            [data["codUbica"]],  # noqa: E501
        )
        if cursor.fetchone()[0] == 0:
            return jsonify({"error": "El código de ubicación no existe"}), 400

        # Check if email exists
        cursor.execute(
            "SELECT COUNT(*) FROM Usuario WHERE email = :1", [data["email"]]
        )  # noqa: E501
        if cursor.fetchone()[0] > 0:
            return jsonify({"error": "El email ya está registrado"}), 400

        # Insert new user
        cursor.execute(
            """
            INSERT INTO Usuario (
                consecUser, nombre, apellido, usuario, 
                fechaRegistro, email, celular, codUbica
            )
            VALUES (
                :1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7, :8
            )
        """,
            [
                data["consecUser"],
                data["nombre"],
                data["apellido"],
                data["usuario"],
                data["fechaRegistro"],
                data["email"],
                data["celular"],
                data["codUbica"],
            ],
        )
        connection.commit()
        return jsonify({"message": "Usuario registrado"})
    except Exception as e:
        if connection:
            connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            connection.close()


@app.route("/setup", methods=["GET"])
def setup_database():
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Execute migrations.sql
        # with open("db/migrations.sql", "r") as f:
        #     migrations = f.read()
        #     for statement in migrations.split(";"):
        #         if statement.strip():
        #             cursor.execute(statement)

        # Execute dataTest.sql
        with open("db/dataTest.sql", "r") as f:
            test_data = f.read()
            for statement in test_data.split(";"):
                if statement.strip():
                    cursor.execute(statement)

        connection.commit()
        return jsonify(
            {
                "message": "Setup completed successfully",
                "details": {"migrations": "Executed", "testData": "Inserted"},
            }
        )
    except Exception as e:
        if connection:
            connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    app.run(port=3001, debug=True)
