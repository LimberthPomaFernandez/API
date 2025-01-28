import os
from fastapi import FastAPI, HTTPException
import sqlite3 as sql

from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


#1- Endpoint para añadir  un nuevo usuario
@app.post('/propietario/add_cliente/{dni}/{nombre}/{email}/{telefono}')
async def addCliente(dni: str, nombre: str, email: str, telefono: str):
  
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (dni, nombre, email, telefono) VALUES (?, ?, ?, ?);", (dni, nombre, email, telefono))
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()
  
  
  return {'message' : 'Cliente añadido correctamente'}



#2- Endpoint para listar todos los clientes y devolverlos formateados
@app.get('/propietario/listar_clientes')
async def listarClientes():
  
  conexion = sql.connect('./DataBase/aplicacion.db')
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM clientes")
  clientes = cursor.fetchall()
  conexion.close()
  
  lista_clientes = []
  for cliente in clientes:
    lista_clientes.append({
      'nombre': cliente[1],
      'dni': cliente[0],
      'email': cliente[2],
      'telefono': cliente[3]
    })
  
  return {'clientes' : lista_clientes}


#3- Endpoint para listar los trabajadores
@app.get('/propietario/listar_trabajadores')
async def listarTrabajadores():

  conexion = sql.connect('./DataBase/aplicacion.db')
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM trabajadores")
  trabajadores = cursor.fetchall()
  conexion.close()
  lista_trabajadores = []
  for trabajador in trabajadores:
    lista_trabajadores.append({
      'nombre': trabajador[1],
      'dni': trabajador[2],
      'email': trabajador[3],
      'antiguedad': trabajador[4],
      'salario': trabajador[5],
      'tipo_trabajador': trabajador[0]
    })
  return {'trabajadores' : trabajadores}




#4- Endpoint para añdir un nuevo vehiculo a un cliente
@app.post('/cliente/registrar_vehiculo/{cliente_dni}/{matricula}/{marca}/{modelo}/{tipo_vehiculo}')
async def registrarVehiculo(cliente_dni: str, matricula: str, marca: str, modelo: str, tipo_vehiculo: str):
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')  
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO vehiculos VALUES ('{matricula}', '{marca}', '{modelo}', '{tipo_vehiculo}', '{cliente_dni}');")
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  return {'message' : 'Vehiculo añadido correctamente'}

#4.1- Endpoint para listar los vehiculos de un cliente
@app.get('/cliente/listar_vehiculos/{cliente_dni}')
async def listarVehiculos(cliente_dni: str):
  lista_vehiculos = []
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM vehiculos WHERE dni_cliente = '{cliente_dni}'")
    vehiculos = cursor.fetchall()
    conexion.close()
    for vehiculo in vehiculos:
      lista_vehiculos.append({
        'matricula': vehiculo[0],
        'marca': vehiculo[1],
        'modelo': vehiculo[2],
        'tipo_vehiculo': vehiculo[3],
        'cliente_id': vehiculo[4]
    })
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  
  return {'vehiculos' : lista_vehiculos}


# Endpoint para listar las tareas
@app.get('/cliente/listar_tareas')
async def listarTareas():
  lista_tareas = []
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM tareas")
    tareas = cursor.fetchall()
    conexion.close()
    for tarea in tareas:
      lista_tareas.append({
        'tarea_id': tarea[0],
        'descripcion': tarea[1],
        'tipo': tarea[2],
        'matricula': tarea[3],
        'estado': tarea[4],
        'mecanico_dni': tarea[5],
        'coste': tarea[6]
    })
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  
  return {'tareas' : lista_tareas}

#5-  Endpoint para una tarea de mantenimiento o reparacion
@app.post('/cliente/addTarea/{descripcion}/{tipo}/{matricula}/{coste}/{dni_cliente}')
async def addTarea( descripcion: str, tipo: str, matricula: str, coste: float, dni_cliente: str):
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    # Comprobar que el vehiculo existe en la tabla vehiculos
    cursor.execute(f"SELECT * FROM vehiculos WHERE matricula = '{matricula}'")
    vehiculo = cursor.fetchone()
    if vehiculo is None:
      return {'message' : 'El vehiculo no existe'}
    
    # Comprobar que el vehiculo pertenezca al cliente
    print(f"Verificando vehículo con matrícula: {matricula} y DNI del cliente: {dni_cliente}")
    cursor.execute("SELECT * FROM vehiculos WHERE matricula = ? AND dni_cliente = ?", (matricula, dni_cliente))
    vehiculo = cursor.fetchone()
    if vehiculo is None:
        return {'message': 'El vehiculo no pertenece al cliente'}
  
    
    # El tipo solo puede ser 'mantenimiento' o 'reparacion'
    if tipo != 'mantenimiento' and tipo != 'reparacion':
      return {'message' : 'El tipo solo puede ser mantenimiento o reparacion'}
    
    # Insertar la tarea
    cursor.execute(f"INSERT INTO tareas VALUES (NULL, '{descripcion}', '{tipo}', '{matricula}', 'no empezada', 'NULL', {coste});")
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  return {'message' : 'Tarea añadida correctamente'}


#6-  Endpoint para listar todas tareas pendientes
@app.get('/trabajador/listar_tareas_pendientes')
async def listarTareasPendientes():
  lista_tareas = []
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM tareas WHERE estado = 'no empezada' OR estado = 'en proceso'")
    tareas = cursor.fetchall()
    conexion.close()
    for tarea in tareas:
      lista_tareas.append({
        'tarea_id': tarea[0],
        'descripcion': tarea[1],
        'tipo': tarea[2],
        'matricula': tarea[3],
        'estado': tarea[4],
        'mecanico_dni': tarea[5],
        'coste': tarea[6]
    })
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  
  return {'tareas' : lista_tareas}

# 6.1 Endpoint para listar las tareas finalizadas
@app.get('/trabajador/listar_tareas_finalizadas')
async def listarTareasFinalizadas():
  lista_tareas = []
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM tareas WHERE estado = 'finalizada'")
    tareas = cursor.fetchall()
    conexion.close()
    for tarea in tareas:
      lista_tareas.append({
        'tarea_id': tarea[0],
        'descripcion': tarea[1],
        'tipo': tarea[2],
        'matricula': tarea[3],
        'estado': tarea[4],
        'mecanico_dni': tarea[5],
        'coste': tarea[6]
    })
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  
  return {'tareas' : lista_tareas}

#7-  Endpoint para agregar un mecanico a una tarea
@app.post('/trabajador/agregar_mecanico_tarea/{tarea_id}/{mecanico_dni}')
async def agregarMecanicoTarea(tarea_id: int, mecanico_dni: str):
  
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    
    # Verificar que la tarea existe
    cursor.execute(f"SELECT * FROM tareas WHERE tarea_id = {tarea_id}")
    tarea = cursor.fetchone()
    if tarea is None:
      return {'message' : 'La tarea no existe'}
    
    # Verificar que el mecanico ya tiene una tarea asignada
    cursor.execute(f"SELECT * FROM tareas WHERE dni_trabajador = '{mecanico_dni}' AND estado = 'en proceso'")
    tarea = cursor.fetchone()
    if tarea is not None:
      return {'message' : 'El mecanico ya tiene una tarea asignada'}
    
    # Verificar que el mecanico existe 
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{mecanico_dni}'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El mecanico no existe'}
    
    # Verificar que el mecanico es un mecanico 
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{mecanico_dni}' AND tipo_trabajador = 'mecanico'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El Trabajador no es un mecanico'}
    
    
    # Verificar que la tarea no ha sido asignada
    cursor.execute(f"SELECT * FROM tareas WHERE tarea_id = {tarea_id} AND estado = 'no empezada'")
    tarea = cursor.fetchone()
    if tarea is None:
      return {'message' : 'La tarea no existe o ya ha sido asignada'}
    
    cursor.execute(f"UPDATE tareas SET dni_trabajador = '{mecanico_dni}' WHERE tarea_id = {tarea_id}")
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  return {'message' : 'Mecanico añadido correctamente'}



#8-  Endpoint para dar por finalizada una tarea
@app.post('/trabajador/finalizar_tarea/{tarea_id}/{mecanico_dni}')
async def finalizarTarea(tarea_id: int, mecanico_dni: str):
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    
    # Verificar que la tarea existe
    cursor.execute(f"SELECT * FROM tareas WHERE tarea_id = {tarea_id}")
    tarea = cursor.fetchone()
    if tarea is None:
      return {'message' : 'La tarea no existe'}
    
    # Verificar que el mecanico existe
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{mecanico_dni}'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El mecanico no existe'}
    
    # En caso que la tarea sea una de reparacion, solo la puede finalizar un supervisor
    cursor.execute(f"SELECT * FROM tareas WHERE tarea_id = {tarea_id} AND tipo = 'reparacion'")
    tarea = cursor.fetchone()
    if tarea is not None:
      cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{mecanico_dni}' AND tipo_trabajador = 'supervisor'")
      mecanico = cursor.fetchone()
      if mecanico is None:
        return {'message' : 'Solo un supervisor puede finalizar una tarea de reparacion'}
    
    # Verificar que la tarea esta en proceso
    cursor.execute(f"SELECT * FROM tareas WHERE tarea_id = {tarea_id} AND estado = 'en proceso'")
    tarea = cursor.fetchone()
    if tarea is None:
      return {'message' : 'La tarea no existe o ya ha sido finalizada'}
    
    
    
    # Actualizar el estado de la tarea
    cursor.execute(f"UPDATE tareas SET estado = 'finalizada' WHERE tarea_id = {tarea_id}")
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()

  return {'message' : 'Tarea finalizada correctamente'}



# Endpoint para borrar Clientes
@app.delete('/propietario/borrar_cliente/{dni}/{dni_trabajador}')
async def deleteCliente(dni: str, dni_trabajador: str):
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    
    # Verificar que el cliente existe
    cursor.execute(f"SELECT * FROM clientes WHERE dni = '{dni}'")
    cliente = cursor.fetchone()
    if cliente is None:
      return {'message' : 'El cliente no existe'}
    
    # Verificar que el trabajador existe
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{dni_trabajador}'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El trabajador no existe'}
    
    # Verificar que el trabajadro es un supervisors
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{dni_trabajador}' AND tipo_trabajador = 'supervisor'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El trabajador no es un supervisor'}
    
    
    cursor.execute(f"DELETE FROM clientes WHERE dni = '{dni}'")
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()
  return {'message' : 'Cliente eliminado correctamente'}


# Endpoint para borrar tareas
@app.delete('/propietario/borrar_tarea/{tarea_id}/{dni_trabajador}')
async def deleteTarea(tarea_id: int, dni_trabajador: str):
  try:
    conexion = sql.connect('./DataBase/aplicacion.db')
    cursor = conexion.cursor()
    
    # Verificar que la tarea existe
    cursor.execute(f"SELECT * FROM tareas WHERE tarea_id = {tarea_id}")
    tarea = cursor.fetchone()
    if tarea is None:
      return {'message' : 'La tarea no existe'}
    
    # Verificar que el trabajador existe
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{dni_trabajador}'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El trabajador no existe'}
    
    # Verificar que el trabajadro es un supervisors
    cursor.execute(f"SELECT * FROM trabajadores WHERE dni = '{dni_trabajador}' AND tipo_trabajador = 'supervisor'")
    mecanico = cursor.fetchone()
    if mecanico is None:
      return {'message' : 'El trabajador no es un supervisor'}
    
    cursor.execute(f"DELETE FROM tareas WHERE tarea_id = {tarea_id}")
    conexion.commit()
  except Exception as e:
    conexion.rollback()
  finally:
    conexion.close()
  
  return {'message' : 'Tarea eliminada correctamente'}


@app.get("/descargar_fichero/{codigo_usr}/{tipo_dato}/{contrasena}")
def descargar_fichero(codigo_usr: str, tipo_dato: str, contrasena: str):
    # Ruta base del directorio de datos del usuario
    ruta_base = os.path.join('datos', f'datos_usuario_{codigo_usr}')

    if not os.path.exists(ruta_base):
        raise HTTPException(status_code=404, detail="Directorio del usuario no encontrado")

    # Ruta del archivo que contiene la información del usuario
    archivo_info = os.path.join(ruta_base, f'informacion_usuario_{codigo_usr}.txt')

    if not os.path.exists(archivo_info):
        raise HTTPException(status_code=404, detail="Archivo de información del usuario no encontrado")

    # Extraer la contraseña del archivo de información
    try:
        with open(archivo_info, 'r') as f:
            lineas = f.readlines()
        contrasena_guardada = None
        for linea in lineas:
            if "contrasenya:" in linea:
                contrasena_guardada = linea.split("contrasenya:")[1].strip()
                break
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el archivo de información: {str(e)}")

    if contrasena != contrasena_guardada:
        raise HTTPException(status_code=403, detail="Contraseña incorrecta")

    # Seleccionar el archivo correcto según el tipo de dato
    if tipo_dato == 'Genetica_Usuario':
        ruta_fichero = os.path.join(ruta_base, f'genetica_usuario_{codigo_usr}.txt')
    else:
        ruta_fichero = os.path.join(ruta_base, f'informacion_usuario_{codigo_usr}.txt')

    if not os.path.exists(ruta_fichero):
        raise HTTPException(status_code=404, detail="Archivo solicitado no encontrado")

    # Enviar el archivo si todo está correcto
    return FileResponse(ruta_fichero)


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)