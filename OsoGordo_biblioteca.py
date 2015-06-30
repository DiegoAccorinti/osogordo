# -*- coding: utf-8 -*-
import pilas

# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
import random
import datetime
sys.path.insert(0, "..")

# Importo funciones desde un archivo ya que ese código es reutilizado en varias escenas.
from chat import *
# Cargo el último estado guardado
from savegame import *

class EscenaBiblioteca(pilas.escena.Base):


	def iniciar(self):

		#Cargo los datos guardados en disco para sincronizar los valores.
		alegria, salud, comida, puntos = leerValores()		

		# HORARIO
		""" chequeo qué hora es para poner al oso gordo a dormir o no """
		ahora = datetime.datetime.now()

		# Creo el fondo
		fondo = pilas.imagenes.cargar('pics/fondo_biblioteca.png')
		actorFondo = pilas.actores.Actor(fondo)
		actorFondo.z = 1000

		#HUE
		texto_personalizado = pilas.actores.Texto("Oso Gordo", magnitud=60, fuente="fuentes/fuente.ttf", y=250, x=-320)
		titulo_puntos = pilas.actores.Texto("puntos", magnitud=20, fuente="fuentes/fuente.ttf", y=280, x=470)
		texto_puntos = pilas.actores.Texto(str(puntos), magnitud=40, fuente="fuentes/fuente.ttf", y=240, x=440)
		#Barras
		barra_alegria = pilas.actores.Energia(progreso = int(alegria), color_relleno = pilas.colores.Color(56,255,75),
		ancho=160, alto=25, con_sombra = False, con_brillo = False)
		barra_alegria.rotacion = -90
		barra_alegria.x = 480
		barra_alegria.y = 98

		barra_salud = pilas.actores.Energia(progreso = int(salud), color_relleno = pilas.colores.Color(56,255,75),
		ancho=160, alto=25, con_sombra = False, con_brillo = False)
		barra_salud.rotacion = -90
		barra_salud.x = 450
		barra_salud.y = 98

		barra_comida = pilas.actores.Energia(progreso = int(comida), color_relleno = pilas.colores.Color(56,255,75),
		ancho=160, alto=25, con_sombra = False, con_brillo = False)
		barra_comida.rotacion = -90
		barra_comida.x = 420
		barra_comida.y = 98

		icono_comida = pilas.actores.Actor(pilas.imagenes.cargar("pics/jamon.png"), x=418, y=0)
		icono_comida.escala = pilas.interpolar([1, 1.5, 1,1.2,1], 1, demora = 1.5)

		icono_alegria = pilas.actores.Actor(pilas.imagenes.cargar("pics/alegria.png"), x=482, y=0)
		icono_alegria.escala = pilas.interpolar([1, 1.5, 1,1.2,1], 1, demora = 1)

		icono_limpieza = pilas.actores.Actor(pilas.imagenes.cargar("pics/limpieza.png"), x=450, y=0)
		icono_limpieza.escala = pilas.interpolar([1, 1.5, 1,1.2,1], 1, demora = 2)

		#cartel habitacion
		img_cartel = pilas.imagenes.cargar('pics/cartel_biblioteca.png')
		cartel = pilas.actores.Actor(img_cartel, x=360, y=-244)

		#cambiar de habitacion
		botonIzq = pilas.actores.Boton(ruta_normal = 'pics/cursorIzq.png', ruta_over = 'pics/cursorIzq_over.png', x=250, y=-244)

		def cuando_pulsan_el_boton():
			from OsoGordo import EscenaDespensa
			pilas.cambiar_escena(EscenaDespensa())
		def cuando_pasa_sobre_el_boton():
			botonIzq.pintar_sobre()
		def cuando_deja_de_pulsar():
			botonIzq.pintar_normal()

		"""botonDer = pilas.actores.Boton(ruta_normal = 'pics/cursorDer.png', ruta_over = 'pics/cursorDer_over.png', x=470, y=-244)

		def cuando_pulsan_el_boton_der():
			pilas.cambiar_escena(EscenaBanio())
		def cuando_pasa_sobre_el_boton_der():
			botonDer.pintar_sobre()
		def cuando_deja_de_pulsar_der():
			botonDer.pintar_normal()"""

		# EL OSO

		if (ahora.hour >= 14 and ahora.hour < 16) or (ahora.hour >= 3 and ahora.hour < 9):
			""" Si son entre las 2 de la tarde y las 4, el oso duerme la siesta.
				A las doce de la noche se duerme hasta las 9 de la mañana."""

		else:

			imagenOso = pilas.imagenes.cargar("pics/osoGordo_original.png")
			oso = pilas.actores.Actor(imagenOso, x=20, y=360)
			oso.radio_de_colision = 100
			oso.centro = (530,290)
			oso.z = 1
			oso.y = [35],0.5
			oso.y = 35
			img_rostro = pilas.imagenes.cargar("pics/rostros/gran_sonrisa.png")
			rostro = pilas.actores.Actor(img_rostro, x=20, y=500)
			rostro.y = [78],0.5
			rostro.y = 78

			#el fondo se sacude al caer
			actorFondo.x = pilas.interpolar([10, -10, 5, 0], 0.2, demora = 0.5)
			actorFondo.y = pilas.interpolar([30, -40, 20, 0], 0.2, demora = 0.5)
			oso.y = pilas.interpolar([45,35], 0.15, demora = 0.5)
			rostro.y = pilas.interpolar([100,78], 0.15, demora = 0.5)

			# Creamos los elementos
			img_disquettes = pilas.imagenes.cargar("pics/disquettes.png")
			disquettes = pilas.actores.Actor(img_disquettes, x=-450, y=-235)
			disquettes.aprender(pilas.habilidades.Arrastrable)
			disquettes.sonido = 'sonidos/larry.ogg'
			disquettes.alegria = 9
			disquettes.decirAlUsar = ['Mi primera PC fue una 386 con dos megabytes de RAM.',u'¿jugaste alguna vez a "The Secret of Monkey Island" ?', u'¿No sabés dónde está Carmen San Diego?']

			img_joystick = pilas.imagenes.cargar("pics/atari2600.png")
			joystick = pilas.actores.Actor(img_joystick, x=-350, y=-235)
			joystick.aprender(pilas.habilidades.Arrastrable)
			joystick.sonido = 'sonidos/atari.ogg'
			joystick.alegria = 10
			joystick.decirAlUsar = [u'¿Cómo saco al ET del pozo?']

			img_commodore = pilas.imagenes.cargar("pics/commodore.png")
			commodore = pilas.actores.Actor(img_commodore, x=-250, y=-235)
			commodore.aprender(pilas.habilidades.Arrastrable)
			commodore.sonido = ['sonidos/commodore_01.ogg', 'sonidos/commodore_02.ogg', 'sonidos/commodore_03.ogg']
			commodore.alegria = 14
			commodore.decirAlUsar = ['LOAD "*",8','POKE 53280,1','READY.', u'Cuando sea grande quiero ser como Zak Mckracken.']

			img_cd = pilas.imagenes.cargar("pics/CD.png")
			cd = pilas.actores.Actor(img_cd, x=-150, y=-235)
			cd.aprender(pilas.habilidades.Arrastrable)
			cd.sonido = 'sonidos/libro.ogg'
			cd.alegria = 7
			cd.decirAlUsar = [u'Llegando los monos - SUMO', u'El león - Los fabulosos Cadillacs', u'El Amor Después Del Amor - Fito Páez', u'Piano Bar - Charly García', u'Pappo\'s Blues Volumen 2 - Pappo\'s Blues', u'Alta Suciedad - Andrés Calamaro', u'Canción Animal - Soda Stereo', u'La Era De La Boludez - Divididos', u'Oktubre - Patricio Rey y Sus Redonditos de Ricota', u'Artaud - Pescado Rabioso', u'Despedazado por mil partes - La Renga', u'Tercer Arco - Los Piojos', u'Angeles Caidos - Attaque 77', u'Hermética - Ácido Argentino',  u'El Exceso - Flema', u'Valentín Alsina - Dos Minutos', u'Ahí Vamos - Gustavo Cerati', u'La Mosca y la Sopa - Patricio Rey y Sus Redonditos de Ricota']

			img_libro = pilas.imagenes.cargar("pics/libro.png")
			libro = pilas.actores.Actor(img_libro, x=-50, y=-235)
			libro.aprender(pilas.habilidades.Arrastrable)
			libro.sonido = 'sonidos/libro.ogg'
			libro.alegria = 9
			libro.decirAlUsar = [u'Obras Completas - Edgar Allan Poe','Obras Completas - Oscar Wilde', u'Sobre héroes y tumbas - Ernesto Sabato', 'Odisea - Homero','El Hobbit - J.R.Tolkien','Viaje al centro de la tierra - Julio Verne',u'Parque Jurásico - Michael Crichton', 'El viejo y el mar - Ernest Hemingway', u'El túnel - Ernesto Sabato', u'El señor de los anillos - J.R.Tolkien', u'Rayuela - Julio Cortazar', u'Don Quijote de la Mancha - Miguel de Cervantes', u'Poema de Gilgamesh - Anónimo', u'Las mil y una noches - Anónimo', u'Crimen y castigo - Fiódor Dostoievski', u'Cien años de soledad - Gabriel García Márquez', u'El castillo - Franz Kafka', u'1984 - George Orwell', u'El tambor de hojalata - Gunter Grass', u'El Aleph - Jorge Luis Borges']


			elementos = [disquettes, joystick, commodore, cd, libro]


			def divertir(oso, elemento):
				
				#sonido
				# Si el elemento tiene un sonido único, elemento.sonido será una cadena. Sino, será una lista de la cual elijo un elemento al azar.
				if type(elemento.sonido) == str:
					sonido = pilas.sonidos.cargar(elemento.sonido)
				else:
					sonido = pilas.sonidos.cargar(random.choice(elemento.sonido))
				sonido.reproducir()
			
				elemento.eliminar()
				barra_alegria.progreso = [barra_alegria.progreso + elemento.alegria]
				barra_comida.progreso = [barra_comida.progreso - 6]

			
				chat(random.choice(elemento.decirAlUsar), 4)

				#Actualizo el puntaje
				global puntos
				puntos += 10
				texto_puntos.texto = str(puntos)

				#actualizo los datos en disco
				actualizarValores(barra_alegria.progreso + elemento.alegria, barra_salud.progreso, barra_comida.progreso - 6, puntos)

			pilas.mundo.colisiones.agregar(oso, elementos, divertir)
		#Control de habitaciones
		botonIzq.conectar_presionado(cuando_pulsan_el_boton)
		botonIzq.conectar_sobre(cuando_pasa_sobre_el_boton)
		botonIzq.conectar_normal(cuando_deja_de_pulsar)
		"""botonDer.conectar_presionado(cuando_pulsan_el_boton_der)
		botonDer.conectar_sobre(cuando_pasa_sobre_el_boton_der)
		botonDer.conectar_normal(cuando_deja_de_pulsar_der)"""

# Para que ande igual si solo ejecuto solo esta escena
if __name__ == "__main__":
	pilas.iniciar(ancho=1024, alto=600)
	pilas.cambiar_escena(EscenaBiblioteca())
	pilas.ejecutar()
