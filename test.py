import script
import unittest

class TestMathFuncs(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(script.fibo(1), 1)

class TestStrFuncs(unittest.TestCase):
    def test_username(self):
        self.assertEqual(script.username('hovno@gmail.com'), 'hovno')

if __name__ == '__main__':
    unittest.main()