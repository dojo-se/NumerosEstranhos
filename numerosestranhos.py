import unittest

def is_estranho(numero):
    def get_divisores(num):
        lista = []
        for i in range(1,num):
            if num % i == 0:
                lista.append(i)  
        return lista 
    
    def sum_array(lista):
        soma = 0
        for i in lista :
            soma += i
        return soma
        
    if sum_array(get_divisores(numero)) > numero:  
        return True
    else:
        return False

def estranhos_ate(numero):
    lista = []
    for i in range(numero + 1):
        if (is_estranho(i)):
           lista.append(i)
    return lista    
 
class TestNumerosEstranhos(unittest.TestCase):
    def test_listaNumeros(self):
        self.assertEqual([12], estranhos_ate(12))        
        
    def test_listaNumerosVazio(self):
        self.assertEqual([], estranhos_ate(5))        


if __name__ == '__main__':
    unittest.main()	
