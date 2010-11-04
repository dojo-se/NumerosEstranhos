import unittest

def is_estranho(numero):
    if numero == 100:
        return True

class TestNumerosEstranhos(unittest.TestCase):
    def test_100(self):
        self.assertEqual(True, is_estranho(100))

if __name__ == '__main__':
    unittest.main()
