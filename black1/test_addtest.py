# Файл: test_addtest.py 12 2

import unittest
from addtest import add_test

class MyTestCase(unittest.TestCase):
    def test_add_3_and_9(self):
        # Mock input to return 3 and 9
        inputs = iter([3, 9])
        def mock_input(prompt):
            return next(inputs)
        add_test.input = mock_input

        self.assertEqual(add_test(), 12)

    def test_add_5_and_5(self , mock_input=None):
        inputs = iter([5, 5])
        add_test.input = mock_input

        self.assertEqual(add_test(), 10)

    def test_add_50_and_8(self):
        inputs = iter([50, 8])
        add_test.input = mock_input


        self.assertEqual(add_test(), 58)

    def test_add_40_and_3(self):
        inputs = iter([40, 3])
        add_test.input = mock_input

        self.assertEqual(add_test(), 43)

if __name__ == '__main__':
    unittest.main()
