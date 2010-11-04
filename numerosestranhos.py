import unittest

def is_estranho(numero):
    def get_divisores(num):
        lista = []
        
        for i in range(1,num):
            if num % i == 0:
                lista.append(i)  
                #print i 
        return lista 
    
    def sum_array(lista):
        soma = 0
        #print lista
        for i in lista :
            soma += i
        return soma
        
    if sum_array(get_divisores(numero)) > numero:  
        return True
    else:
        return False
        
    
 
class TestNumerosEstranhos(unittest.TestCase):
    def test_100(self):
        self.assertEqual(True, is_estranho(100))
        
    def test_13(self):
        self.assertEqual(False, is_estranho(13))        

if __name__ == '__main__':
    unittest.main()
