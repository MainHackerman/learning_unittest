import script
import unittest

class TestMathFuncs(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(script.fibo(1), 1)

if __name__ == '__main__':
    unittest.main()