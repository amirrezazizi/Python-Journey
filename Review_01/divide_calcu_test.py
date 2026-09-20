import unittest
from divide_calcu import divide

class TestDivide(unittest.TestCase):
    def test_int(self):
        a = 10
        b = 5
        res = 2
        self.assertEqual(divide(a,b) , res)
    def test_float(self):
        a = 4.8
        b = 2
        res = 2.4
        self.assertEqual(divide(a,b) , res)
    def test_divide_by_zero(self):
        a = 10
        b = 0
        self.assertRaises(ZeroDivisionError,divide, a , b)
    def test_typeError_a(self):
        a = "10"
        b = 5
        self.assertRaises(TypeError , divide, a , b )
    def test_typeError_b(self):
        a = 10
        b = "5"
        self.assertRaises(TypeError , divide , a , b)
    def test_typeBool(self):
        a = True
        b = 5
        self.assertRaises(TypeError , divide , a , b)
    

if __name__ == "__main__":
    unittest.main()