import unittest
from countc import countc

class Testcountc(unittest.TestCase):
    def test_simple(self):
        s = 'amir'
        c = 'a'
        result = 1
        self.assertEqual(countc(s, c),result)
    def test_nullString(self):
        s = ''
        c = 'a'
        result= 0
        self.assertEqual(countc(s, c), result)
    def test_nothing(self):
        s = 'this hxs no x in it !!!'
        c = 'a'
        result = 0
        self.assertEqual(countc(s, c), result)
    def test_upper_lower(self):
        s = 'Amir rezA And a'
        c = 'a'
        result = 1
        self.assertEqual(countc(s, c),result)

if __name__== "__main__":
    unittest.main()