import unittest
from factorial import fact_module

class TestFactorial(unittest.TestCase):
    def test_fact_zero(self):
        res = fact_module(0)
        self.assertEqual(res,1)

    def test_fact_one(self):
        res = fact_module(1)
        self.assertEqual(res,1)

    def test_fact_positive(self):
        res = fact_module(5)
        self.assertEqual(res,120)

    def test_fact_negative(self):
        res = fact_module(-5)
        self.assertEqual(res,0)
    

if __name__ == '__main__':
    unittest.main()