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
        
    return sum_array(get_divisores(numero)) > numero

def estranhos_ate(numero):
    lista = []
    for i in range(numero + 1):
        if (is_estranho(i)):
           lista.append(i)
    return lista    
 
class TestNumerosEstranhos(unittest.TestCase):
    def test_lista_numeros_estranhos_ate_12(self):
        self.assertEqual([12], estranhos_ate(12))        
        
    def test_lista_numeros_estranhos_ate_5(self):
        self.assertEqual([], estranhos_ate(5))
        
    def test_lista_numeros_estranhos_ate_19(self):
        self.assertEqual([12,18], estranhos_ate(19))        


if __name__ == '__main__':
    unittest.main()	
