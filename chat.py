# -*- coding: utf-8 -*-
import pilas
import sys
import random
sys.path.insert(0, "..")


def chat(texto, borrar_en_segundos):

	img_globo = pilas.imagenes.cargar('pics/globo.png')
	globo = pilas.actores.Actor(img_globo, x= -27, y = 200)
	globo.transparencia = 20
	globo.escala_y = 2
	globo.escala_x = 47
	img_globo_pico = pilas.imagenes.cargar('pics/globo_pico.png')
	globoPico = pilas.actores.Actor(img_globo_pico, x= 162, y = 161)
	globoPico.transparencia = 20
	texto_a_decir = pilas.actores.Texto(u""+texto, magnitud=20, fuente="fuentes/globo.ttf", y=200, x=0)
	#borro el globo			
	pilas.escena_actual().tareas.una_vez(borrar_en_segundos, texto_a_decir.eliminar)
	pilas.escena_actual().tareas.una_vez(borrar_en_segundos, globo.eliminar)
	pilas.escena_actual().tareas.una_vez(borrar_en_segundos, globoPico.eliminar)
