import unittest

def setUpModule(): 
    print("Comenzando Prueba...")

def tearDownModule(): 
    print("Adios")   

class MisPruebas(unittest.TestCase): 
    def test_caso_1(self): 
        self.assertEqual("amigo" == "AMIGO".lower(), True) 
    
    def test_caso_2(self): 
        self.assertEqual(5+5, 25) 
    
if __name__ == "__main__":
    unittest.main()