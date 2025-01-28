
import os, shutil, random

def crear_sistema_carpetas(ruta, num_usuarios=1):

	# Primero comprobamos si el sistema de carpetas ya existe:
	if os.path.exists(ruta+"/datos"):

		# Si ya existe, lo eliminamos:
		shutil.rmtree(ruta+"/datos")

	# Una vez hecha la comprobacion anterior, creamos todo desde cero:
	os.mkdir(ruta + "/datos")

	# A continuacion, para cada usuario...
	for id_usuario in range(num_usuarios):

		# Creamos la carpeta con la informacion de cada usuario:
		os.mkdir(ruta+"/datos/datos_usuario_"+str(id_usuario).zfill(4))

def generar_contraseña():

    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    especiales = "!@#$%^&*()-_"

    contrasena = ""

    # contraseña de estructura fija: letra > número > car especial
    for _ in range(4):
        contrasena += random.choice(letras)
        contrasena += random.choice(numeros)
        contrasena += random.choice(especiales)

    return contrasena



def inventar_informacion_usuario(fichero):

	# Creamos una lista de nombres y apellidos:
	nombres = ["Alejandro", "Beatriz", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Ignacio", "Juana", "Kevin", "Luis", "Marta", "Nicolas", "Olga", "Pablo", "Raquel", "Sergio", "Teresa", "Victor", "Yago"]
	apellidos = ["Alvarez", "Bartolome", "Cabo", "Gonzalez", "Rodriguez", "Perez", "Lopez", "Martinez", "Garcia", "Fernandez", "Sanchez", "Romero", "Diaz", "Torres", "Valdes", "Vargas", "Prieto", "Ruiz", "Gomez", "Jimenez", "Moreno", "Alvarez", "Bolaños", "Castro", "Herrera", "Hurtado"]

	# Escogemos al azar un nombre para el usuario:
	nombre = random.choice(nombres)
	apellido1 = random.choice(apellidos)
	apellido2 = random.choice(apellidos)

	# Generamos aleatoriamente una edad:
	edad = random.randint(18, 65)

	# Generamos aleatoriamente un numero de telefono:
	telefono = random.randint(600000000, 699999999)

	# Generamos su direccion de correo electronico:
	email = nombre.lower() + "_" + apellido1.lower() + "_" + apellido2.lower() + "@mail.com"

	# Escribimos toda la informacion en el fichero:

	fichero.write("INFORMACION DEL USUARIO\n\n")
	fichero.write(f"Nombre completo: {nombre} {apellido1} {apellido2}\n")
	fichero.write(f"Edad: {edad}\n")
	fichero.write(f"Telefono movil: {telefono}\n")
	fichero.write(f"Correo Electronico: {email}\n")
	fichero.write(f'contrasenya: {generar_contraseña()}')

def inventar_genetica_usuario(fichero):

	nucleotidos = ["A", "T", "G", "C"]

	# Aleatorizamos un poco la composicion de los nucleótidos del usuario:
	nucleotidos_usuario = nucleotidos
	for _ in range(16):
		nucleotidos_usuario.append(random.choice(nucleotidos))

	# Nos inventamos un numero de filas:
	num_filas = random.randint(7500, 25000)

	# Para cada una de las filas...
	for _ in range(num_filas):

		composicion_fila = ""

		for x in range(1, 17):

			composicion_fila += random.choice(nucleotidos_usuario)

			if x % 4 == 0:

				composicion_fila += "-"

		fichero.write(composicion_fila[:-1]+"\n")



def poblar_carpetas(ruta):

	# Comprobamos que el sistema de carpetas existe:
	if not os.path.exists(ruta+"/datos"):

		print("Error. El sistema de carpetas no existe.")
		return
	
	# Como esta funcion no sabe cuantos usuarios hay, listamos el directorio:
	l_usuarios = os.listdir(ruta+"/datos")

	# Ahora, para cada usuario:
	for usuario in l_usuarios:

		# Creamos un fichero con su informacion personal:
		f_info = open(ruta+"/datos/"+usuario+"/informacion_"+usuario[-12:]+".txt", "w")

		print(f"\tGenerando informacion del usuario {usuario[-4:]}...")

		# Llamamos a la funcion que se inventa la informacion del usuario:
		inventar_informacion_usuario(f_info)
		f_info.close()

		# Ahora creamos un fichero con su informacion genetica:
		f_gen = open(ruta+"/datos/"+usuario+"/genetica_"+usuario[-12:]+".txt", "w")

		print(f"\tGenerando genetica del usuario {usuario[-4:]}...")

		# Llamamos a la funcion que se inventa la informacion genetica del usuario:
		inventar_genetica_usuario(f_gen)
		f_gen.close()


if __name__ == "__main__":

	# Primero imprimimos por pantalla un pequeño mensaje de bienvenida:
	print("Bienvenido al programa para generar automaticamente")
	print("una base de datos de ficheros simulando el ADN de")
	print("diferentes seres humanos (inventados)")

	# En segundo lugar preguntamos al usuario cuántos seres humanos quiere
	# que se invente el programa
	while True:
	
		num_usuarios = input("Por favor, introduce cuantos usuarios quieres generar para la base de datos: ")

		try:
			num_usuarios = int(num_usuarios)

			# Le metemos un "por si acaso" para que el usuario no se flipe:
			if num_usuarios > 0 and num_usuarios <= 9999:
				break
			else:
				print("Error: el numero de usuarios introducido no es valido, prueba otra vez.")

		except ValueError:
			print("Error: No se puede convertir la variable a un entero.")

	# En tercer lugar llamamos a la funcion que se va a encargar de crear el sistema de carpetas
	# (antes le pasamos el directorio en el que estamos, que en el que queremos que cree la base de datos):

	ruta = os.getcwd()
	
	crear_sistema_carpetas(ruta, num_usuarios)

	# En cuarto lugar, una vez que el sistema de carpetas se ha creado, lo rellenamos con informacion inventada:

	poblar_carpetas(ruta)