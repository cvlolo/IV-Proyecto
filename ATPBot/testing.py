
import db
import scraping
import unittest

class Database(unittest.TestCase):
	def testConsultar(self):
		error=db.consultar_jugador("Rafael Nadal")
		self.assertEqual(error,-1)

	def testInsertar(self):
		lista=[]
		db.insertar_jugador("Vardy","15")
		lista=db.consultar_jugador("Vardy")
		print(lista)
		self.assertEqual(lista[0], "Vardy")

	def testBorrar(self):
		lista=[]
		db.borrar_jugador("Vardy")
		lista=db.consultar_jugador("Vardy")
		self.assertEqual(lista,-1)
		
		
		
		
if __name__ == '__main__':
    unittest.main()
