import unittest
from app import say_hello

class TestApp(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("Alice"), "Hello, Alice!")
        self.assertEqual(say_hello("Bob"), "Hello, Bob!")

if __name__ == '__main__':
    unittest.main()