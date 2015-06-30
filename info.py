import pilas
import sys
import random
sys.path.insert(0, "..")

class EscenaInfo(pilas.escena.Base):

    def iniciar(self):
        fondo = pilas.imagenes.cargar('pics/info.png')
        infoFondo = pilas.actores.Actor(fondo)

        opcion_uno = pilas.actores.Boton(ruta_normal = 'pics/menu_volver.png', ruta_over = 'pics/menu_volver_over.png')
        opcion_uno.x = 410
        opcion_uno.y = -260

	# MENU

	def cuando_pulsan_opcion_uno():
		pilas.recuperar_escena() # vuelvo al menu principal

	def cuando_pasa_sobre_opcion_uno():
		opcion_uno.pintar_sobre()
		opcion_uno.escala = ([1.3],0.1)

	def cuando_deja_de_pulsar_opcion_uno():
		opcion_uno.escala = ([1],0.1)

	opcion_uno.conectar_presionado(cuando_pulsan_opcion_uno)
	opcion_uno.conectar_sobre(cuando_pasa_sobre_opcion_uno)
	opcion_uno.conectar_normal(cuando_deja_de_pulsar_opcion_uno)


# Para que ande igual si solo ejecuto solo esta escena
if __name__ == "__main__":
	pilas.iniciar(ancho=1024, alto=600)
	pilas.cambiar_escena(EscenaInfo())
	pilas.ejecutar()
