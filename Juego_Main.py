import Enemigo
import os
import random

def main():
	Enemigos = []
	for i in range(5):
		enem_random = random.randint(0, len(Enemigo.ENEMIGOS)-1)
		if enem_random == Enemigo.PALADIN:
			Enemigos.append(Enemigo.paladin())
		if enem_random == Enemigo.CAMPEON:
			Enemigos.append(Enemigo.campeon())
		if enem_random == Enemigo.BALLESTA:
			Enemigos.append(Enemigo.ballesta())

	Heroe = {
	'nombre': 'William Wallas',
	'ataque': 10,
	'puntos_vida': 100
	}

	RECUPERAR_VIDA = 5
	MAS_ATAQUE = 3
	contador = 1

	def Heroe_atacar(enemigo):
		if enemigo == 'Paladin':
			print(f'Tu ataque ha disminuido en 2 por estar enfrentando a {enemigo}')
			Ataque_acturalizado = Heroe['ataque'] - 2
			print(f'Has causado {Ataque_acturalizado} de daño')
			return Ataque_acturalizado
		elif enemigo == 'Ballesta':
			print(f'Tu ataque ha aumentado en 4 por estar enfrentando a {enemigo}')
			Ataque_acturalizado = Heroe['ataque'] + 4
			print(f'Has causado {Ataque_acturalizado} de daño')
			return Ataque_acturalizado
		else:
			print(f'Has causado {Heroe["ataque"]} de daño')
			return Heroe["ataque"]
	

	while Heroe['puntos_vida'] > 0 and len(Enemigos) > 0:
		while Heroe['puntos_vida'] > 0 and Enemigos[0].vida > 0:
			print(f'Heroe HP: {Heroe["puntos_vida"]}')
			print(f'{Enemigos[0].nombre} HP: {Enemigos[0].vida}')
			Enemigos[0].atacar()
			Heroe['puntos_vida'] -= Enemigos[0].ataque
			if Enemigos[0].nombre == 'Paladin':
				Heroe['puntos_vida'] -= Enemigos[0].locura
			if Heroe['puntos_vida'] > 0 and len(Enemigos) > 0:
				Ataque_actualizado = Heroe_atacar(Enemigos[0].nombre)
				Enemigos[0].vida = Enemigos[0].vida - Ataque_actualizado
				input('Contiunar con la batalla')
				print('\n')
		if Enemigos[0].vida <= 0:
			print(f'\nHas derrotado al mounstruo numero {contador}')
			print(f'{Enemigos[0].nombre} HP al ser derrotado: {Enemigos[0].vida}')
			print(f'Heroe HP restantes: {Heroe["puntos_vida"]}')
			print(f'Tu ataque ha aumentado en {MAS_ATAQUE}')
			print(f'Tus puntos de vida se han recuperado en {RECUPERAR_VIDA}')
			Heroe['ataque'] += 3
			Heroe['puntos_vida'] += 5
			contador += 1
			Enemigos.pop(0)
			if len(Enemigos) > 0:
				input ('Ha por el siguiente mounstruo')
				print('\n')
			else:
				print('\n')
				input('Contiunar con la batalla')
				contador -= 1
				print(f'\nFELICITACIONES.\nHas derrotado a los {contador} mounstruos. Bien Hecho!')
		else:
			input('Contiunar con la batalla')
			print(f'\nHas sido derrotado')
			print(f'\n{Enemigos[0].nombre} te ha derrotado. HP restantes del enemigo: {Enemigos[0].vida}')
			print(f'HP Heroe al ser derrotado: {Heroe["puntos_vida"]}\n')
	print("FIN. GRACIAS POR JUGAR")
	
if __name__ == '__main__':
	main()