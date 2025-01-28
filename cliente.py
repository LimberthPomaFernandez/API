# Empezar a comprobar los endpoints de cliente.py
import os
import shutil
import requests

def add_cliente(dni,nombre,telefono,email):
  try:
    response = requests.post(f"http://127.0.0.1:8000/propietario/add_cliente/{dni}/{nombre}/{email}/{telefono}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")


def listar_clientes():
  response = requests.get("http://127.0.0.1:8000/propietario/listar_clientes")
  print(response.json())
  

def listar_trabajadores():
  response = requests.get("http://127.0.0.1:8000/propietario/listar_trabajadores")
  print(response.json())

                  
def registrar_vehiculo(cliente_dni,matricula,marca,modelo,tipo_vehiculo):

  try:
    response = requests.post(f"http://127.0.0.1:8000/cliente/registrar_vehiculo/{cliente_dni}/{matricula}/{marca}/{modelo}/{tipo_vehiculo}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")


def listar_vehiculos(cliente_dni):
  try:
    response = requests.get(f"http://127.0.0.1:8000/cliente/listar_vehiculos/{cliente_dni}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")


def listar_tareas():
  try:
    response = requests.get(f"http://127.0.0.1:8000/cliente/listar_tareas")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")


def addTarea(matricula,coste,description,tipo,dni_cliente):
  try:
    response = requests.post(f"http://127.0.0.1:8000/cliente/addTarea/{description}/{tipo}/{matricula}/{coste}/{dni_cliente}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")


def listar_tareas_pendientes():
  try:
    response = requests.get(f"http://127.0.0.1:8000/trabajador/listar_tareas_pendientes")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")

def listar_tareas_finalizadas():
  try:
    response = requests.get(f"http://127.0.0.1:8000/trabajador/listar_tareas_finalizadas")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")

def agregarMecanicoTarea(dni,id_tarea):
  try:
    response = requests.post(f"http://127.0.0.1:8000/trabajador/agregar_mecanico_tarea/{id_tarea}/{dni}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")
    
    
def finalizarTarea(tarea_id,dni_trabajador):
  try:
    response = requests.post(f"http://127.0.0.1:8000/trabajador/finalizar_tarea/{tarea_id}/{dni_trabajador}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")
      
      
def borrarCliente(dni_trabajador,dni_cliente):
  try:
    response = requests.delete(f"http://127.0.0.1:8000/propietario/borrar_cliente/{dni_cliente}/{dni_trabajador}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")
    
def borrarTarea(tarea_id,dni_trabajador):
  try:
    response = requests.delete(f"http://127.0.0.1:8000/propietario/borrar_tarea/{tarea_id}/{dni_trabajador}")
    response.raise_for_status()
    print(f'{response.json()}')
  except requests.exceptions.RequestException as e:
    print(f"Error adding cliente: {e}")
      
      
def descargar_archivo(codigo_usr, tipo_dato, contrasena):
    url = f'http://127.0.0.1:8000/descargar_fichero/{codigo_usr}/{tipo_dato}/{contrasena}'
    response = requests.get(url)
    
    if response.status_code == 200:
        if not os.path.exists("./descargas"):
          os.mkdir("./descargas")
        

        nombre_archivo = f'descargas/usuario_{codigo_usr}-{tipo_dato}.txt'
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        print(f'Archivo descargado con éxito: {nombre_archivo}')
    elif response.status_code == 403:
        print('Contraseña incorrecta')
    elif response.status_code == 404:
        print('Archivo o usuario no encontrado')
    else:
        print('Error en la descarga del fichero:', response.status_code)
      
salir = False
while not salir:
  
  print(""" 1 => Añadir cliente
            2 => Listar clientes
            3 => Listar trabajadores
            4 => Registrar vehiculo
            5 => Listar vehiculos por DNI
            6 => Listar tareas
            7 => Añadir tarea nueva
            8 => Listar tareas pendientes
            9 => Listar tareas finalizadas
            10 => Agregar mecanico a tarea
            11 => Finalizar tarea
            12 => Borrar cliente
            13 => Borrar tarea
            14 => Descargar Fichero
            15 => Salir""")

  opcion = int(input("Introduce una opcion: "))

  if opcion == 1:
    
    dni = input("Introduce el DNI del cliente: ")
    nombre = input("Introduce el nombre del cliente: ")
    email = input("Introduce el email del cliente: ")
    telefono = input("Introduce el telefono del cliente: ")
    add_cliente(dni,nombre,telefono,email)
  elif opcion == 2:
    
    listar_clientes()
  elif opcion == 3:
    
    listar_trabajadores()
  elif opcion == 4:
    
    cliente_dni = input("Introduce el DNI del cliente: ")
    matricula = input("Introduce la matricula del vehiculo: ")
    marca = input("Introduce la marca del vehiculo: ")
    modelo = input("Introduce el modelo del vehiculo: ")
    tipo_vehiculo = input("Introduce el tipo de vehiculo: ")
    registrar_vehiculo(cliente_dni,matricula,marca,modelo,tipo_vehiculo)
  elif opcion == 5:
    
    cliente_dni = input("Introduce el DNI del cliente: ")
    listar_vehiculos(cliente_dni)
  elif opcion == 6:
    
    listar_tareas()
  elif opcion == 7:
    
    matricula = input("Introduce la matricula del vehiculo: ")
    coste = input("Introduce el coste de la tarea: ")
    description = input("Introduce la descripcion de la tarea: ")
    tipo = input("Introduce el tipo de la tarea (reparacion / mantenimiento): ")
    dni_cliente = input("Introduce el DNI del cliente: ")
    
    addTarea(matricula,coste,description,tipo,dni_cliente)
  elif opcion == 8:
    
    listar_tareas_pendientes()
  elif opcion == 9:
    
    listar_tareas_finalizadas()
  elif opcion == 10:
    
    id_tarea = int(input("Introduce el id de la tarea: "))
    dni = input("Introduce el DNI del mecanico: ")
    
    agregarMecanicoTarea(dni, id_tarea)
  elif opcion == 11:
    
    tarea_id= int(input("Introduce el id de la tarea: "))
    dni_trabajador=input("Introduzca su dni para poder borrar la tarea: ")
    finalizarTarea(tarea_id,dni_trabajador)
  elif opcion == 12:
    
    dni_trabajador = input("Introduzca su dni para poder borrar el cliente: ")
    dni_cliente = input("Introduce el DNI del cliente que se borrara: ")
    borrarCliente(dni_trabajador,dni_cliente)
  elif opcion == 13:
    
    dni_trabajador = input("Introduzca su dni para poder borrar la tarea: ")
    tarea_id = int(input("Introduce el id de la tarea: "))
    borrarTarea(tarea_id,dni_trabajador)
    
  elif opcion == 14:
    codigo_usr = input('Ingrese el codigo del usuario: ')
    contrasena = input('Ingrese la contrasenya del usuario: ')

    tipo_dato = input('Ingrese el tipo de fichero que quieres:\n 1 =>(Informacion Usuario) \n 2 => (Genetica Usuario) \n: ')
    
    if tipo_dato == '1':
        descargar_archivo(codigo_usr, 'Informacion_usuario', contrasena)
    elif tipo_dato == '2':
        descargar_archivo(codigo_usr, 'Genetica_Usuario', contrasena)
    else:
        print('Por favor, elija una de las opciones disponibles')

  elif opcion == 15:
    print("Hasta luego")
    salir = True  
  else:
    print("Opcion no valida")