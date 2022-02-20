import unittest

from src.main import reproducir

class TestLagoMusical(unittest.TestCase):
    
    def test_sound(self):
        """
        Comprueba que se obtengan los sonidos correctos.
        """
        self.assertListEqual(['fiu', 'cric-cric', 'brrah'], reproducir('brr'))
        self.assertListEqual(['trri-trri', 'croac'], reproducir('birip'))
        self.assertListEqual(['cric-cric', 'brrah'], reproducir('plop'))
    
    def test_dont_sound(self):
        """	
        Comprueba que no se obtengan sonidos.	
        """
        self.assertListEqual([], reproducir('croac'))
        self.assertListEqual([], reproducir('brrah'))

    def test_unrecognized_sound(self):
        """
        Comprueba que la función valide que un sonido no existe.
        """
        self.assertIsNone(reproducir('aaaa'))

if __name__ == '__main__':
    unittest.main()