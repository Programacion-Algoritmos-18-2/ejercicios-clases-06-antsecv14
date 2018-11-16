#Se importa el abc para poder realizar los abstracts
import abc
class PersonaEquipo(metaclass=abc.ABCMeta):
	__metaclass__ = abc.ABCMeta

	def __init__(self, nom):
		self.nombre = nom

	@abc.abstractmethod

	def entrenar():
		pass

"""
	def __init__(self):
		self.nombre = ""
	
	def AgregarNombre(self,n):
		self.nombre = n
	
	def ObtenerNombre(self):
		return self.nombre

	def entrenar(self):
		print("Entreno")
"""	
#La clase futbolista que es hija de la clase PersonaEquipo
class Futbolista(PersonaEquipo):

	def __init__(self,nom):
		super(Futbolista,self).__init__(nom)
		self.posicion_campo = ""

	def agregar_posicion_campo(self,p):
		self.posicion_campo = p

	def obtener_posicion_campo(self):
		return self.posicion_campo

	def entrenar(self):
		print("Yo %s, Futbolista, hago practica en el entrenamiento"% self.nombre)


#La clase Entrenador que es hija de la clase PersonaEquipo
class Entrenador(PersonaEquipo):
	def __init__(self,nom):
		super(Entrenador,self).__init__(nom)
		self.codigo_entrenador = ""

	def agregar_codigo_Entrenador(self,c):
		self.codigo_entrenador = c

	def obtener_codigo_entrenador(self):
		return self.codigo_entrenador

	def entrenar(self):
		print("yo %s, Entrenador, entreno a los jugadores"% self.nombre)

#La clase Medico_Equipo que es hija de la clase PersonaEquipo
class Medico_Equipo(PersonaEquipo):

	def __init__(self, nom):
		super(Medico_Equipo, self).__init__(nom)
		self.titulo=""

	def entrenar(self):
		print("yo %s,Medigo, atiendo a los jugadores en el entrenamiento"% self.nombre)

#La clase Presidente que es hija de la clase PersonaEquipo
class Presidente(PersonaEquipo):

	def __init__(self, nom):
		super(Presidente, self).__init__(nom)
		self.propiedades=""

	def entrenar(self):
		print("yo %s, Presidente, pongo el dinero para el entrenamiento"% self.nombre)
