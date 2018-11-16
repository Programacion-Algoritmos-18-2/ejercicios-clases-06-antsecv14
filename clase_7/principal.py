#Se importa modelado del archivo paquete
from paquete.modelado import *
#p = PersonaEquipo("Luis")
e2 = Futbolista("Juan")
e3 = Entrenador("Pedro")
e4 = Medico_Equipo("David")
e5 = Presidente("Mario")

lista = (e2, e3, e4, e5)
for l in lista:
	l.entrenar()
""""ador()
persona = PersonaEquipo()
persona.AgregarNombre("jose")
persona.entrenar()
f = Futbolista()
f.AgregarNombre("Maria")
f.entrenar()
e = Entrenador()
e.AgregarCodigoEntrenador("Hernan")
e.entrenar()
"""