import sqlite3, os


# Si la base de datos existe, la borramos para empezar de cero:
if os.path.isfile("./DataBase/aplicacion.db"):
    os.remove("./DataBase/aplicacion.db")

# Al conectarnos a la base de datos, la creamos de cero:
conexion = sqlite3.connect("./DataBase/aplicacion.db")

# Creamos la tabla "clientes":
conexion.execute("""CREATE TABLE clientes(
                        dni                 varchar(9)         PRIMARY KEY,
                        nombre              varchar(50)        NOT NULL,
                        email               varchar(50)        NOT NULL,
                        telefono            varchar(15)        NOT NULL
);""")

# Creamos la tabla "vehiculos":
conexion.execute("""CREATE TABLE vehiculos(
                        matricula           varchar(8)         PRIMARY KEY,
                        marca               varchar(20)        NOT NULL,
                        modelo              varchar(20)        NOT NULL,
                        tipo_vehiculo       varchar(20)        NOT NULL,
                        dni_cliente         varchar(9)         NOT NULL,
                        FOREIGN KEY(dni_cliente) REFERENCES clientes(dni)
);""")

# Creamos la tabla "trabajadores":
conexion.execute("""CREATE TABLE trabajadores(
                        dni                 varchar(9)         PRIMARY KEY,
                        nombre              varchar(50)        NOT NULL,
                        email               varchar(50)        NOT NULL,
                        antiguedad          int                NOT NULL,
                        salario             float              NOT NULL,
                        tipo_trabajador     varchar(20)        NOT NULL
);""")

# Creamos la tabla "tareas":
conexion.execute("""CREATE TABLE tareas(
                        tarea_id            integer PRIMARY KEY AUTOINCREMENT,
                        descripcion         text               NOT NULL,
                        tipo                varchar(20)        NOT NULL,
                        matricula           varchar(15)        NOT NULL,
                        estado              varchar(20)        NOT NULL,
                        dni_trabajador      varchar(9)         ,
                        coste               float              NOT NULL,
                        FOREIGN KEY(matricula) REFERENCES vehiculos(matricula)
                        FOREIGN KEY(dni_trabajador) REFERENCES trabajadores(dni)

);""")

conexion.commit()

print('Base de datos creada, cerrando conexion. . .')

conexion.close()
