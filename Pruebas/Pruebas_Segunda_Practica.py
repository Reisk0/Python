import unittest

def setUpModule(): 
    print("Hola desde metodo")

def tearDownModule(): 
    print("Adios desde metodo")   

class testMyModule(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print("Hola desde clase")
    @classmethod
    def tearDownClass(cls):
        print("Hola desde clase")
    
    def test_caso_1(self): 
        self.assertEqual("amigo" == "AMIGO".lower(), True) 
    
    def test_caso_2(self): 
        self.assertEqual(5+5, 25) 
    
if __name__ == "__main__":
    unittest.main()
