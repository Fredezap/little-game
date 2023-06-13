
PALADIN = 0
CAMPEON = 1
BALLESTA = 2

ENEMIGOS = [PALADIN,CAMPEON,BALLESTA]

class enemigo(object):
	def __init__(self, nombre='', arma='', vida=5, ataque=5):
		super(enemigo, self).__init__()
		self._nombre = nombre
		self._arma = arma
		self._vida = vida
		self._ataque = ataque

	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self, valor):
		self._nombre = valor
	
	@property
	def arma(self):
		return self._arma
	@arma.setter
	def arma(self, valor):
		self._arma = valor

	@property
	def vida(self):
		return self._vida
	@vida.setter
	def vida(self, valor):
		self._vida = valor

	@property
	def ataque(self):
		return self._ataque
	@ataque.setter
	def ataque(self, valor):
		self._ataque = valor

	def atacar(self):
		print (f'''{self._nombre} te esta atacando con {self._arma} y te ha hecho {self._ataque} de daño''')

class paladin(enemigo):
	def __init__(self, nombre='', arma='', vida=5, ataque=5):
		super().__init__('Paladin','Espada a caballo',15,14)
		self._locura = 10

	@property
	def locura(self):
		return self._locura
	@locura.setter
	def locura(self, valor):
		self._locura = locura
		
	def atacar(self):
		super().atacar()
		print (f'Ademas te genero {self._locura} de daño extra')

class campeon(enemigo):
	def __init__(self, nombre='', arma='', vida=5, ataque=5):
		super().__init__('Campeon','Espada',12,8)

class ballesta(enemigo):
	def __init__(self, nombre='', arma='', vida=5, ataque=5):
		super().__init__('Ballesta','arco',14,6)