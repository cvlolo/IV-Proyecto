import clasePrueba
import unittest

class TestingClass(unittest.TestCase):
	def test_primerTest(self):
		self.assertTrue(0 <= clasePrueba.extraerPuntuacion("Rafael Nadal") <= 50000)
		self.assertEqual(clasePrueba.extraerPuntuacion("Rafael Nadal"), 9875)
		self.assertTrue(isinstance(clasePrueba.mostrarRanking(), str))
		self.assertTrue(clasePrueba.mostrarRanking() != "")
		
if __name__ == '__main__':
    unittest.main()
