import pilas
import webbrowser
from OsoGordo import EscenaDespensa
from info import EscenaInfo

#Inicio PILAS
pilas.iniciar(ancho=1024, alto=600, titulo='Oso Gordo')

class EscenaDeMenu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):

        class GirarPorSiempre(pilas.habilidades.Habilidad):
            def __init__(self, receptor):
                self.receptor = receptor
            def actualizar(self):
                self.receptor.rotacion += 0.1

        img_back = pilas.imagenes.cargar('pics/back.jpg')
        back = pilas.actores.Actor(img_back, x=0, y=0)
        back.escala = 1.3
        back.aprender(GirarPorSiempre)


        presentacion = pilas.imagenes.cargar('pics/presentacion.png')
        presFondo = pilas.actores.Actor(presentacion)


        opcion_uno = pilas.actores.Boton(ruta_normal = 'pics/menu_opcion_uno.png', ruta_over = 'pics/menu_opcion_uno_over.png')
        opcion_uno.x = 390
        opcion_uno.y = -30

        opcion_dos = pilas.actores.Boton(ruta_normal = 'pics/menu_opcion_dos.png', ruta_over = 'pics/menu_opcion_dos_over.png')
        opcion_dos.x = 435
        opcion_dos.y = -80

        opcion_tres = pilas.actores.Boton(ruta_normal = 'pics/menu_opcion_tres.png', ruta_over = 'pics/menu_opcion_tres_over.png')
        opcion_tres.x = 427
        opcion_tres.y = -130

        opcion_facebook = pilas.actores.Boton(ruta_normal = 'pics/menu_opcion_facebook.png', ruta_over = 'pics/menu_opcion_facebook_over.png')
        opcion_facebook.x = 450
        opcion_facebook.y = -180

	# MENU

	#####  NO SE Como pasar el valor introducido a otra escena.	
	#nombre = pilas.interfaz.IngresoDeTexto(ancho=400, x=390, y=10)
	#nombre.limite_de_caracteres = 12
	#nombre.solo_letras()
	#nombre.texto = "Ingresa un nombre para tu Oso Gordo"



	def cuando_pulsan_opcion_uno():
		intro.detener()  # Paro la musica de la intro
		pilas.cambiar_escena(EscenaDespensa()) # Cambio a la escena Despensa

	def cuando_pasa_sobre_opcion_uno():
		opcion_uno.pintar_sobre()
		opcion_uno.escala = ([1.3],0.1)

	def cuando_deja_de_pulsar_opcion_uno():
		opcion_uno.escala = ([1],0.1)

	def cuando_pulsan_opcion_dos():
		pilas.almacenar_escena(EscenaInfo())

	def cuando_pasa_sobre_opcion_dos():
		opcion_dos.pintar_sobre()
		opcion_dos.escala = ([1.3],0.1)

	def cuando_deja_de_pulsar_opcion_dos():
		opcion_dos.escala = ([1],0.1)

	def cuando_pulsan_opcion_tres():
		import sys
		sys.exit(0)

	def cuando_pasa_sobre_opcion_tres():
		opcion_tres.pintar_sobre()
		opcion_tres.escala = ([1.3],0.1)

	def cuando_deja_de_pulsar_opcion_tres():
		opcion_tres.escala = ([1],0.1)

	def cuando_pulsan_opcion_facebook():
		webbrowser.open_new('https://www.facebook.com/mascotaosogordo')

	def cuando_pasa_sobre_opcion_facebook():
		opcion_facebook.pintar_sobre()
		opcion_facebook.escala = ([1.2],0.1)

	def cuando_deja_de_pulsar_opcion_facebook():
		opcion_facebook.escala = ([1],0.1)

	opcion_uno.conectar_presionado(cuando_pulsan_opcion_uno)
	opcion_uno.conectar_sobre(cuando_pasa_sobre_opcion_uno)
	opcion_uno.conectar_normal(cuando_deja_de_pulsar_opcion_uno)

	opcion_dos.conectar_presionado(cuando_pulsan_opcion_dos)
	opcion_dos.conectar_sobre(cuando_pasa_sobre_opcion_dos)
	opcion_dos.conectar_normal(cuando_deja_de_pulsar_opcion_dos)

	opcion_tres.conectar_presionado(cuando_pulsan_opcion_tres)
	opcion_tres.conectar_sobre(cuando_pasa_sobre_opcion_tres)
	opcion_tres.conectar_normal(cuando_deja_de_pulsar_opcion_tres)

	opcion_facebook.conectar_presionado(cuando_pulsan_opcion_facebook)
	opcion_facebook.conectar_sobre(cuando_pasa_sobre_opcion_facebook)
	opcion_facebook.conectar_normal(cuando_deja_de_pulsar_opcion_facebook)

# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
import random
sys.path.insert(0, "..")

intro = pilas.musica.cargar("sonidos/coleco_music.ogg")
intro.reproducir(repetir=True)
pilas.cambiar_escena(EscenaDeMenu())
pilas.ejecutar()
