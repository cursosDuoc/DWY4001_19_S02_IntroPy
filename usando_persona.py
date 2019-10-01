#! /usr/bin/python3

# guardar en la carpeta del proyecto como 'usando_persona.py'

# del archivo (modulo) Persona.py importamos (la clase) Persona
from Persona import Persona

# Ahora en el "main", voy a crear un objeto y voy a llamar al método
perrin = Persona("Juan Eduardo Lopez", "12365789-2")
perrin.imprimir()

# En python los atributos son siempre publicos...
# y por eso los puedo modificar...
perrin.rut = "19233221-7"
perrin.imprimir()

# Sin embargo hay una convencion-> si un atributo parte con _
# los programadores Python lo tratan como si fuera privado.
# perrin._nombre = "Juan Lopez" -> esto no se hace!


# Voy a crear una persona leyendo desde la consola:
nombre = input("Ingrese su nombre:")
rut = input("Ingrese su rut:")
persona_nueva = Persona(nombre, rut)
persona_nueva.imprimir()