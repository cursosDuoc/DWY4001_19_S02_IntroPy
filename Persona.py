#!/usr/bin/python3

# guardar en la carpeta del proyecto como :
# 'Persona.py'

class Persona:
	""" Clase que representa a una Persona
		En Chile!
		self -> rol similar al this de Java
		El contructor se llama siempre 
		(doble underscore)init(doble underscore)
		Todas las operaciones de la clase reciben
		al self como primer parametro!!!
	"""
	def __init__(self, nombre, rut):		
		self._nombre = nombre
		self.rut = rut

	# OJO todos los métodos reciben el self como parametro!	
	def imprimir(self):
		texto = " ".join(["soy", self._nombre, ", mi rut es",self.rut ])
		print(texto)














