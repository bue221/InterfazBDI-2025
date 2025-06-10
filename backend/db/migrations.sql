-- Tabla TipoUbica
CREATE TABLE TipoUbica (
  codTipoUbica VARCHAR2(3) PRIMARY KEY,
  descTipoUbica VARCHAR2(20)
);

-- Tabla Ubicacion
CREATE TABLE Ubicacion (
  codUbica VARCHAR2(4) PRIMARY KEY,
  nomUbica VARCHAR2(30),
  tipoUbica VARCHAR2(3),
  ubica_sup VARCHAR2(4),
  FOREIGN KEY (tipoUbica) REFERENCES TipoUbica(codTipoUbica),
  FOREIGN KEY (ubica_sup) REFERENCES Ubicacion(codUbica)
);

-- Tabla Usuario
CREATE TABLE Usuario (
  consecUser VARCHAR2(5) PRIMARY KEY,
  nombre VARCHAR2(25),
  apellido VARCHAR2(25),
  usuario VARCHAR2(6),
  fechaRegistro DATE,
  email VARCHAR2(50),
  celular VARCHAR2(16),
  codUbica VARCHAR2(4),
  FOREIGN KEY (codUbica) REFERENCES Ubicacion(codUbica)
);