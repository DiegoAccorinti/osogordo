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

class EscenaBanio(pilas.escena.Base):

	def iniciar(self):

		#Cargo los datos guardados en disco para sincronizar los valores.
		alegria, salud, comida, puntos = leerValores()	

		print "puntos al cargar la escena: " + str(puntos)	

		# HORARIO
		""" chequeo qué hora es para poner al oso gordo a dormir o no """
		ahora = datetime.datetime.now()

		#SONIDOS
		snd_cepillo = pilas.sonidos.cargar("sonidos/cepilloDientes.ogg")
		snd_enjuague = pilas.sonidos.cargar("sonidos/enjuague.ogg")

		# Creo el fondo
		fondo = pilas.imagenes.cargar('pics/fondo_banio.png')
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
		img_cartel = pilas.imagenes.cargar('pics/cartel_banio.png')
		cartel = pilas.actores.Actor(img_cartel, x=360, y=-244)

		#cambiar de habitacion
		"""botonIzq = pilas.actores.Boton(ruta_normal = 'pics/cursorIzq.png', ruta_over = 'pics/cursorIzq_over.png', x=250, y=-244)

		def cuando_pulsan_el_boton():
			ppilas.almacenar_escena(EscenaBiblioteca())
		def cuando_pasa_sobre_el_boton():
			botonIzq.pintar_sobre()
		def cuando_deja_de_pulsar():
			botonIzq.pintar_normal()"""

		botonDer = pilas.actores.Boton(ruta_normal = 'pics/cursorDer.png', ruta_over = 'pics/cursorDer_over.png', x=470, y=-244)

		def cuando_pulsan_el_boton_der():
			from OsoGordo import EscenaDespensa
			pilas.cambiar_escena(EscenaDespensa())
		def cuando_pasa_sobre_el_boton_der():
			botonDer.pintar_sobre()
		def cuando_deja_de_pulsar_der():
			botonDer.pintar_normal()

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
			img_esponja = pilas.imagenes.cargar("pics/esponja.png")
			esponja = pilas.actores.Actor(img_esponja, x=-450, y=-245)
			esponja.aprender(pilas.habilidades.Arrastrable)
			esponja.sonido = 'sonidos/ducha.ogg'
			esponja.salud = 23
			esponja.cuantahambreda = 9
			esponja.decirAlUsar = [u'¡NO!, ¡armas químicas NO!', u'Bañame solo de frente para hacer más rápido.', u'¡¡¡Hace chui!!!']

			img_cepillo = pilas.imagenes.cargar("pics/cepilloDientes.png")
			cepillo = pilas.actores.Actor(img_cepillo, x=-330, y=-245)
			cepillo.aprender(pilas.habilidades.Arrastrable)
			cepillo.sonido = 'sonidos/cepilloDientes.ogg'
			cepillo.salud = 12
			cepillo.cuantahambreda = 2
			cepillo.decirAlUsar = [u'El dentífrico con sabor a frutilla no se come.']

			img_enjuague = pilas.imagenes.cargar("pics/enjuague.png")
			enjuague = pilas.actores.Actor(img_enjuague, x=-255, y=-235)
			enjuague.aprender(pilas.habilidades.Arrastrable)
			enjuague.sonido = 'sonidos/enjuague.ogg'
			enjuague.salud = 5
			enjuague.cuantahambreda = 2
			enjuague.decirAlUsar = [u'¿El gusto ácido es normal?', u'Este líquido parece adulterado...', 'El color verde me da mala espina..', u'gggggddd me parece que tragué un poco', u' aaaajjjj  por favor, comprá de otro gusto', 'Si pierdo los dientes es tu culpa']

			elementos = [esponja, cepillo, enjuague]


			def limpiar(oso, elemento):
			
				elemento.eliminar()

				#sonido
				# Si el elemento tiene un sonido único, elemento.sonido será una cadena. Sino, será una lista de la cual elijo un elemento al azar.
				if type(elemento.sonido) == str:
					sonido = pilas.sonidos.cargar(elemento.sonido)
				else:
					sonido = pilas.sonidos.cargar(random.choice(elemento.sonido))
				sonido.reproducir()

				#gota_pic = pilas.imagenes.cargar("pics/gota.png")
				#gota = pilas.actores.Actor(gota_pic)
				#gotas = pilas.actores.Estrella() * 5
				#gotas.aprender(pilas.habilidades.Llover)

				barra_salud.progreso = [barra_salud.progreso + elemento.salud]
				barra_comida.progreso = [barra_comida.progreso - elemento.cuantahambreda]

				chat(random.choice(elemento.decirAlUsar), 4)

				#Actualizo el puntaje
				global puntos
				print "puntos anteriores: " + str(puntos)				
				puntos += 10
				texto_puntos.texto = str(puntos)

				#actualizo los datos en disco
				actualizarValores(barra_alegria.progreso, barra_salud.progreso + elemento.salud, barra_comida.progreso - elemento.cuantahambreda, puntos)

			pilas.mundo.colisiones.agregar(oso, elementos, limpiar)

		#Control de habitaciones
		"""botonIzq.conectar_presionado(cuando_pulsan_el_boton)
		botonIzq.conectar_sobre(cuando_pasa_sobre_el_boton)
		botonIzq.conectar_normal(cuando_deja_de_pulsar)"""
		botonDer.conectar_presionado(cuando_pulsan_el_boton_der)
		botonDer.conectar_sobre(cuando_pasa_sobre_el_boton_der)
		botonDer.conectar_normal(cuando_deja_de_pulsar_der)

# Para que ande igual si solo ejecuto solo esta escena
if __name__ == "__main__":
	pilas.iniciar(ancho=1024, alto=600)
	pilas.cambiar_escena(EscenaBanio())
	pilas.ejecutar()
