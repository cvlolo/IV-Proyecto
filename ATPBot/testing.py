import funVarias
import unittest

class Test(unittest.TestCase):
        
        def test_CompIn(self): 
                funVarias.insertarJugador("Pepe",10)
		ptos=funVarias.ObtenerPuntosJugador("Pepe")
		self.assertEqual(ptos,10)

	def test_CompOut(self): 
                funVarias.borrarJugador("Pepe")
		ptos=funVarias.ObtenerPuntosJugador("Pepe")
		self.assertFalse(ptos,10)
		
        def test_CompClas(self):
                self.assertTrue(len(funVarias.ATPClas()) > 0)  #Compruebo que el tamanio de la lista de la clasificacion es 
                                                                            #4 ya que de momento tengo 4 equipos

if __name__ == '__main__':
        unittest.main()
