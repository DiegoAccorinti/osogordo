# -*- coding: utf-8 -*-
import os,sys
import base64
sys.path.insert(0, "..")

# Es la primera vez que juega?

""" Con os.path.exists me fijo si existe el archivo, utilizando os.path.expanduser('~') para ubicar la carpeta home del usuario, cualquiera que sea su nombre """

def actualizarValores(alegria, salud, comida, puntos):
	def normalizar(valor):
		if valor  > 100:
			valor = 100
		if valor < 0:
			valor = 0

		return valor
	alegria = normalizar(alegria)
	salud   = normalizar(salud)
	comida  = normalizar(comida)
	
	f = open (os.path.expanduser('~')+"/.osogordo/savegame.bin", 'w')
	#formateo y ofusco los datos
	""" para alegria, salud y comida tomo la parte entera (el Actor Energía le aporta decimales) y los convierto a cadena """
	datos = '|'.join([str(int(alegria)), str(int(salud)), str(int(comida)), str(puntos)])
	print "Grabo datos : " +datos
	#datos_en_base64 = base64.b64encode(datos)
	datos_en_base64 = datos

	#escribo los datos
	f.write(datos_en_base64)
	f.close

def leerValores():
	#abro el archivo para lectura
	f = open (os.path.expanduser('~')+"/.osogordo/savegame.bin", 'r')
	datos_en_base64 = f.read()
	""" Primero decodificamos la ofuscación en Base64 de los datos,
		luego separamos los valores y se los asignamos a cada variable. """
	#datos = base64.b64decode(datos_en_base64)
	datos = datos_en_base64
	datos = datos.split('|')
	print "Leyendo datos en disco: "
	print datos
	alegria = datos[0]
	salud =   datos[1]
	comida =  datos[2]
	puntos =  int(datos[3])
	return alegria, salud, comida, puntos


if os.path.exists(os.path.expanduser('~')+"/.osogordo/savegame.bin"):

	print "cargando datos anteriores"
	""" Ya jugó, entonces necesitamos recuperar los valores guardados. """
	# llamamos a la función "leerValores" que nos devuelve los cuatro valores guardados.
	alegria, salud, comida, puntos = leerValores()	
	

else:
	""" No jugó nunca, entonces tengo que crear el archivo por primera vez
		y grabarle los valores iniciales de Alegría, Comida y Salud del Oso Gordo. """
	print "primer juego"
	# creo el directorio
	os.mkdir (os.path.expanduser('~')+"/.osogordo")

	actualizarValores(50, 90, 50, 0)

	alegria = 50
	salud = 90
	comida = 50
	puntos = 0

