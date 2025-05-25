import unittest
from hello import my_sum

class test_hello(unittest.TestCase):
    def test_sum(self):
        print("TestSum")
        self.assertEqual(my_sum(3, 2, 6, 1), 12)