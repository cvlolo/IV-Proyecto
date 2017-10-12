


dictionary = {"Roger Federer":7505,"Andy Murray":6290, "Alexander Zverev":4400, "Rafael Nadal":9875}

def extraerPuntuacion(Nombre):
	return dictionary.get(Nombre)

def extraerNombre(puntuacion):
	return dictionary.get(puntuacion)


def mostrarRanking():
	clasif = sorted(dictionary.items(), key=lambda dictionary: dictionary[1])
	string = ""
	for x in clasif:
		string="Nombre: " + x[0] + " Puntuacion: " +str(x[1])+ "\n" + string
		
	return string

	

print mostrarRanking()
