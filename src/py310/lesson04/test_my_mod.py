import unittest
import my_mod


class MyFuncTestCase(unittest.TestCase):
    def test_my_func(self):
        test_val1, test_val2 = 2, 3
        expected = 7
        actual = my_mod.my_func(test_val1, test_val2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
