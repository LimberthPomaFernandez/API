import sqlite3

# Nos conectamos a la base de datos:
conexion = sqlite3.connect("./DataBase/aplicacion.db")

# Poblamos la tabla "clientes":
conexion.execute("INSERT INTO clientes VALUES ('4567543P', 'Roberto', 'roberto@gmail.com', 654897456);")
conexion.execute("INSERT INTO clientes VALUES ('5678765G', 'Antonio', 'antonio@hotmail.com', 674545456);")


# Poblamos la tabla "vehiculos":
conexion.execute("INSERT INTO vehiculos VALUES ('2548-JML', 'Mercedes', 'EQE', 'Berlina', '4567543P');")
conexion.execute("INSERT INTO vehiculos VALUES ('5487-FLJ', 'Citroen', 'C3', 'Compacto', '5678765G');")


# Poblamos la tabla "trabajadores":
conexion.execute("INSERT INTO trabajadores VALUES ('6789347J', 'Rocio', 'rocio.bernabe@tuercaslocas.com', 3, 1647.45, 'supervisor');")
conexion.execute("INSERT INTO trabajadores VALUES ('4890763H', 'Mario', 'mario.gimenez@tuercaslocas.com', 5, 1750.10, 'supervisor');")
conexion.execute("INSERT INTO trabajadores VALUES ('4231453X', 'Daniel', 'daniel.martinez@tuercaslocas.com', 1, 1268.50, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('5745675J', 'Lauren', 'Lauren.tome@tuercaslocas.com', 2, 1365.96, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('6543892L', 'Ana', 'ana.rodriguez@tuercaslocas.com', 4, 1589.30, 'supervisor');")
conexion.execute("INSERT INTO trabajadores VALUES ('8934567M', 'Javier', 'javier.fernandez@tuercaslocas.com', 3, 1620.25, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('5738492P', 'Carla', 'carla.lopez@tuercaslocas.com', 2, 1398.50, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('2346578N', 'Luis', 'luis.gonzalez@tuercaslocas.com', 5, 1800.75, 'supervisor');")
conexion.execute("INSERT INTO trabajadores VALUES ('4567823Q', 'Marta', 'marta.sanchez@tuercaslocas.com', 3, 1500.00, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('7890345R', 'Pablo', 'pablo.diaz@tuercaslocas.com', 1, 1250.00, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('9101123S', 'Sara', 'sara.martinez@tuercaslocas.com', 4, 1705.45, 'supervisor');")
conexion.execute("INSERT INTO trabajadores VALUES ('3345678T', 'Miguel', 'miguel.perez@tuercaslocas.com', 2, 1450.80, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('5556789U', 'Lucia', 'lucia.ramos@tuercaslocas.com', 1, 1200.60, 'mecanico');")
conexion.execute("INSERT INTO trabajadores VALUES ('6789034V', 'Pedro', 'pedro.garcia@tuercaslocas.com', 5, 1820.90, 'supervisor');")


# Poblamos la tabla "tareas":
conexion.execute("INSERT INTO tareas VALUES (NULL, 'Cambiar faro delantero derecho', 'reparacion','2548-JML','en proceso','5745675J', 150.00);")
conexion.execute("INSERT INTO tareas VALUES (NULL, 'Revision de los 25.000', 'mantenimiento','2548-JML','no empezada',NULL, 200.00);")
conexion.execute("INSERT INTO tareas VALUES (NULL, 'Cambio de acite', 'mantenimiento','5487-FLJ','finalizada','NULL', 200.00);")




conexion.commit()
print('Base de datos poblada, cerrando conexion. . .')
conexion.close()
