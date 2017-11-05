import ATPbot
import db
import scraping
import unittest

class Database(unittest.TestCase):
	def test_consultar(self):
		error=db.consultar_jugador("pepe")
		self.assertEqual(error,-1)

	def test_insertar(self):
		lista=[]
		db.insertar_jugador("Vardy","15")
		lista=db.consultar_jugador("Vardy")
		self.assertEqual(lista[0], "Vardy")

	def borrar_jugador(self):
		lista=[]
		db.borrar_jugador("Vardy")
		lista=db.consultar_jugador("Vardy")
		self.assertEqual(lista,-1)
		
		
		
		
if __name__ == '__main__':
    unittest.main()
