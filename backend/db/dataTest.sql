INSERT INTO TipoUbica VALUES ('1', 'Pais');
INSERT INTO TipoUbica VALUES ('2', 'Departamento');
INSERT INTO TipoUbica VALUES ('3', 'Ciudad');
INSERT INTO TipoUbica VALUES ('4', 'Area');
INSERT INTO TipoUbica VALUES ('5', 'Provincia');

INSERT INTO Ubicacion VALUES ('57', 'Colombia', '1', NULL);
INSERT INTO Ubicacion VALUES ('1', 'E.U', '1', NULL);
INSERT INTO Ubicacion VALUES ('34', 'Espana', '1', NULL);
INSERT INTO Ubicacion VALUES ('54', 'Argentina', '1', NULL);

-- Departamentos de Colombia
INSERT INTO Ubicacion VALUES ('05', 'Antioquia', '2', '57');
INSERT INTO Ubicacion VALUES ('81', 'Arauca', '2', '57');
INSERT INTO Ubicacion VALUES ('11', 'Bogota D.C.', '2', '57');

-- Ciudades de Colombia
INSERT INTO Ubicacion VALUES ('15', 'Boyaca', '2', '57');
INSERT INTO Ubicacion VALUES ('25', 'Cundinamarca', '2', '57');

-- Estados de E.U.
INSERT INTO Ubicacion VALUES ('205', 'Alabama', '4', '1');
INSERT INTO Ubicacion VALUES ('907', 'Alaska', '4', '1');
INSERT INTO Ubicacion VALUES ('209', 'California', '4', '1');