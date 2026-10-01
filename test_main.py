"""main.py 的单元测试。"""
import unittest

from main import fibonacci, is_prime


class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_values(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


class TestIsPrime(unittest.TestCase):
    def test_primes(self):
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            self.assertTrue(is_prime(p), p)

    def test_non_primes(self):
        for n in (0, 1, 4, 6, 8, 9, 10, 15, 21):
            self.assertFalse(is_prime(n), n)


if __name__ == "__main__":
    unittest.main()
