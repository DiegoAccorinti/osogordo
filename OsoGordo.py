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

from OsoGordo_banio import EscenaBanio
from OsoGordo_biblioteca import EscenaBiblioteca

class EscenaDespensa(pilas.escena.Base):

	def iniciar(self):

		# HORARIO
		""" chequeo qué hora es para poner al oso gordo a dormir o no """
		ahora = datetime.datetime.now()
		"""for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
			print attr, ':', getattr(d, attr)"""

		#SONIDOS
		mordisco_01 = pilas.sonidos.cargar("sonidos/mordisco_01.wav")
		mordisco_02 = pilas.sonidos.cargar("sonidos/mordisco_02.wav")
		mordisco_03 = pilas.sonidos.cargar("sonidos/mordisco_03.wav")

		# Creo el fondo
		fondo = pilas.imagenes.cargar('pics/fondo.png')
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
		img_cartel = pilas.imagenes.cargar('pics/cartel_despensa.png')
		cartel = pilas.actores.Actor(img_cartel, x=360, y=-244)

		#cambiar de habitacion
		botonIzq = pilas.actores.Boton(ruta_normal = 'pics/cursorIzq.png', ruta_over = 'pics/cursorIzq_over.png', x= 250, y=-244)

		def cuando_pulsan_el_boton():
			pilas.almacenar_escena(EscenaBanio())
		def cuando_pasa_sobre_el_boton():
			botonIzq.pintar_sobre()
		def cuando_deja_de_pulsar():
			botonIzq.pintar_normal()

		botonDer = pilas.actores.Boton(ruta_normal = 'pics/cursorDer.png', ruta_over = 'pics/cursorDer_over.png', x= 470, y=-244)

		def cuando_pulsan_el_boton_der():
			pilas.almacenar_escena(EscenaBiblioteca())
		def cuando_pasa_sobre_el_boton_der():
			botonDer.pintar_sobre()
		def cuando_deja_de_pulsar_der():
			botonDer.pintar_normal()

		# EL OSO

		if (ahora.hour >= 14 and ahora.hour < 15) or (ahora.hour >= 0 and ahora.hour < 9):
			""" Si son entre las 2 de la tarde y las 4, el oso duerme la siesta.
				A las doce de la noche se duerme hasta las 9 de la mañana."""

			grilla = pilas.imagenes.cargar_grilla("pics/durmiendo/durmiendo.png", 2)
			oso = pilas.actores.Animacion(grilla, True, velocidad = 0.65)
			snd_ronquidos = pilas.sonidos.cargar("sonidos/ronquidos2.ogg")
			snd_ronquidos.reproducir(repetir=True)
		else:

			imagenOso = pilas.imagenes.cargar("pics/osoGordo_original.png")
			oso = pilas.actores.Actor(imagenOso, x=20, y=360)
			oso.radio_de_colision = 100
			oso.centro = (530,290)
			oso.z = 1
			oso.y = [35],0.5
			oso.y = 35
			#el fondo se sacude al caer
			actorFondo.x = pilas.interpolar([10, -10, 5, 0], 0.2, demora = 0.5)
			actorFondo.y = pilas.interpolar([30, -40, 20, 0], 0.2, demora = 0.5)
			oso.y = pilas.interpolar([45,35], 0.15, demora = 0.5)


			#boca masticando
			masticando = pilas.imagenes.cargar_grilla("pics/boca/masticando/masticando.png", 9)
		

			# Creamos las bananas y las colocamos en una lista.
			img_banana = pilas.imagenes.cargar("pics/banana.png")
			banana = pilas.actores.Actor(img_banana, x = -450, y = -245)
			banana.aprender(pilas.habilidades.Arrastrable)
			banana.calorias = 15
			banana.loqueensucia = 10
			banana.decirAlUsar = [u'mmmm  con dulce de leche quedaría muy bien',u'¡falta la crema!', 'Banana nou ten carozo.']

			# Creamos la zanahoria
			img_zanahoria = pilas.imagenes.cargar("pics/zanahoria.png")
			zanahoria = pilas.actores.Actor(img_zanahoria, x = -350, y = -245)
			zanahoria.aprender(pilas.habilidades.Arrastrable)
			zanahoria.calorias = 13
			zanahoria.loqueensucia = 7
			zanahoria.decirAlUsar = [u'Muy rica la ensalada..  ¿y el bife cuándo llega?', u'La zanahoria hace bien a la vista. Los choripanes también.']

			# Creamos la hamburguesa
			img_hamburguesa = pilas.imagenes.cargar("pics/hamburguesa.png")
			hamburguesa = pilas.actores.Actor(img_hamburguesa, x = -250, y = -245)
			hamburguesa.aprender(pilas.habilidades.Arrastrable)
			hamburguesa.calorias = 45
			hamburguesa.loqueensucia = 12
			hamburguesa.decirAlUsar = [u'Tremenda Cangreburguer', u'¿Tiene morrón?', u'mmmmm  ¡con mayonesa!', 'Con la comida no se jode, eh.', 'Hola, vine a comer comida.', u'mmmm y después chimichanga.']

			# Creamos el helado
			img_helado = pilas.imagenes.cargar("pics/helado.png")
			helado = pilas.actores.Actor(img_helado, x = -150, y = -245)
			helado.aprender(pilas.habilidades.Arrastrable)
			helado.calorias = 30
			helado.loqueensucia = 20
			helado.decirAlUsar = [u'Lo quiero todo de limón.', u'Super dulce de leche bañado en dulce de leche, por favor...', u'La crema del cielo es crema americana con colorante.', u'Jamás subestimes un gusto, yo pido Vainilla.', u'¿Frutos del bosque? demasiado femenino para mi.', u'Me comí el vacito. Era de telgopor.', u'El helado no lo comparto.']

			elementos = [banana, zanahoria, hamburguesa, helado]

			def comer_comida(oso, elemento):
				x = random.randint (1, 3)
				if x == 1:
					mordisco_01.reproducir()
				elif x == 2:
					mordisco_02.reproducir()
				else:
					mordisco_03.reproducir()

				elemento.eliminar()

				#termino = False
				#boca = pilas.actores.Animacion(masticando, False, x = 34, y = 14)
				#while (termino == False):
				#	termino = boca.avanzar()
				#boca = pilas.imagenes.cargar("pics/boca/normal.png")

				barra_comida.progreso = [barra_comida.progreso + elemento.calorias]
				barra_salud.progreso = [barra_salud.progreso - elemento.loqueensucia]
				chat(random.choice(elemento.decirAlUsar), 2)

				#actualizo los valores en disco
				actualizarValores(barra_alegria.progreso, barra_salud.progreso - elemento.loqueensucia, barra_comida.progreso + elemento.calorias, puntos)


			pilas.mundo.colisiones.agregar(oso, elementos, comer_comida)


		#Control de habitaciones
		botonIzq.conectar_presionado(cuando_pulsan_el_boton)
		botonIzq.conectar_sobre(cuando_pasa_sobre_el_boton)
		botonIzq.conectar_normal(cuando_deja_de_pulsar)
		botonDer.conectar_presionado(cuando_pulsan_el_boton_der)
		botonDer.conectar_sobre(cuando_pasa_sobre_el_boton_der)
		botonDer.conectar_normal(cuando_deja_de_pulsar_der)

# Para que ande igual si solo ejecuto solo esta escena
if __name__ == "__main__":
	pilas.iniciar(ancho=1024, alto=600)
	pilas.cambiar_escena(EscenaDespensa())
	pilas.ejecutar()
