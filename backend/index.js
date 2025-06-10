const express = require('express');
const oracledb = require('oracledb');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const app = express();

app.use(cors());
app.use(express.json());

const dbConfig = {
    user: 'SYS',
    password: 'MiClave123',
    connectString: 'localhost:1521/ORCLCDB',
    privilege: oracledb.SYSDBA
};

app.get('/usuarios', async (req, res) => {
    let connection;
    try {
        connection = await oracledb.getConnection(dbConfig);
        const result = await connection.execute(`SELECT * FROM Usuario`);
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    } finally {
        if (connection) await connection.close();
    }
});

app.post('/usuarios', async (req, res) => {
    const { consecUser, nombre, apellido, usuario, fechaRegistro, email, celular, codUbica } = req.body;
    let connection;
    try {
        connection = await oracledb.getConnection(dbConfig);

        // Check if email already exists
        const checkEmail = await connection.execute(
            'SELECT COUNT(*) as count FROM Usuario WHERE email = :1',
            [email]
        );

        if (checkEmail.rows[0][0] > 0) {
            return res.status(400).json({ error: 'El email ya está registrado' });
        }

        await connection.execute(`
      INSERT INTO Usuario (consecUser, nombre, apellido, usuario, fechaRegistro, email, celular, codUbica)
      VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7, :8)
    `, [consecUser, nombre, apellido, usuario, fechaRegistro, email, celular, codUbica], { autoCommit: true });
        res.json({ message: 'Usuario registrado' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    } finally {
        if (connection) await connection.close();
    }
});

app.get('/setup', async (req, res) => {
    let connection;
    try {
        connection = await oracledb.getConnection(dbConfig);

        // Execute migrations.sql
        const migrationsPath = path.join(__dirname, 'db', 'migrations.sql');
        const migrationsSQL = fs.readFileSync(migrationsPath, 'utf8');
        const migrationStatements = migrationsSQL.split(';').filter(stmt => stmt.trim());

        for (const statement of migrationStatements) {
            if (statement.trim()) {
                await connection.execute(statement);
            }
        }

        // Execute dataTest.sql
        const dataTestPath = path.join(__dirname, 'db', 'dataTest.sql');
        const dataTestSQL = fs.readFileSync(dataTestPath, 'utf8');
        const dataTestStatements = dataTestSQL.split(';').filter(stmt => stmt.trim());

        for (const statement of dataTestStatements) {
            if (statement.trim()) {
                await connection.execute(statement);
            }
        }

        await connection.commit();
        res.json({
            message: 'Setup completed successfully',
            details: {
                migrations: 'Executed',
                testData: 'Inserted'
            }
        });
    } catch (err) {
        console.error('Error during setup:', err);
        res.status(500).json({ error: err.message });
    } finally {
        if (connection) await connection.close();
    }
});

app.listen(3001, () => console.log('API corriendo en http://localhost:3001'));