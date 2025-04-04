import unittest

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        # 测试正数相加
        self.assertEqual(add_numbers(2, 3), 5)
        # 测试负数相加
        self.assertEqual(add_numbers(-1, -1), -2)
        # 测试零的相加
        self.assertEqual(add_numbers(0, 5), 5)

    def test_multiply_numbers(self):
        # 测试正数相乘
        self.assertEqual(multiply_numbers(2, 3), 6)
        # 测试负数相乘
        self.assertEqual(multiply_numbers(-2, 3), -6)
        # 测试零相乘
        self.assertEqual(multiply_numbers(0, 5), 0)

if __name__ == '__main__':
    unittest.main() 