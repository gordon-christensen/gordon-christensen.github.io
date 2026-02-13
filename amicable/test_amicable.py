"""Tests for amicable number computation."""

import unittest

from amicable import find_amicable_pairs, sum_of_amicable_numbers, sum_of_proper_divisors


class TestSumOfProperDivisors(unittest.TestCase):
    """Tests for sum_of_proper_divisors."""

    def test_zero(self):
        self.assertEqual(sum_of_proper_divisors(0), 0)

    def test_one(self):
        self.assertEqual(sum_of_proper_divisors(1), 0)

    def test_prime(self):
        # Proper divisors of a prime p are just {1}
        self.assertEqual(sum_of_proper_divisors(7), 1)
        self.assertEqual(sum_of_proper_divisors(13), 1)
        self.assertEqual(sum_of_proper_divisors(97), 1)

    def test_perfect_square(self):
        # 9: divisors are 1, 3
        self.assertEqual(sum_of_proper_divisors(9), 4)
        # 36: divisors are 1, 2, 3, 4, 6, 9, 12, 18
        self.assertEqual(sum_of_proper_divisors(36), 55)

    def test_composite(self):
        # 12: divisors are 1, 2, 3, 4, 6
        self.assertEqual(sum_of_proper_divisors(12), 16)
        # 28: divisors are 1, 2, 4, 7, 14 (perfect number)
        self.assertEqual(sum_of_proper_divisors(28), 28)

    def test_perfect_numbers(self):
        # Perfect numbers equal the sum of their proper divisors
        for n in (6, 28, 496, 8128):
            with self.subTest(n=n):
                self.assertEqual(sum_of_proper_divisors(n), n)

    def test_amicable_pair_220_284(self):
        # The classic amicable pair: s(220) = 284, s(284) = 220
        self.assertEqual(sum_of_proper_divisors(220), 284)
        self.assertEqual(sum_of_proper_divisors(284), 220)

    def test_two(self):
        # Edge: smallest value with a proper divisor
        self.assertEqual(sum_of_proper_divisors(2), 1)


class TestFindAmicablePairs(unittest.TestCase):
    """Tests for find_amicable_pairs."""

    def test_below_200_returns_empty(self):
        # Smallest amicable pair is (220, 284)
        pairs = list(find_amicable_pairs(200))
        self.assertEqual(pairs, [])

    def test_below_300_finds_220_284(self):
        pairs = list(find_amicable_pairs(300))
        self.assertEqual(pairs, [(220, 284)])

    def test_pairs_are_ordered_a_less_than_b(self):
        for a, b in find_amicable_pairs(10000):
            with self.subTest(a=a, b=b):
                self.assertLess(a, b)

    def test_known_pairs_below_10000(self):
        # All amicable pairs where both members are below 10000
        expected = [
            (220, 284),
            (1184, 1210),
            (2620, 2924),
            (5020, 5564),
            (6232, 6368),
        ]
        pairs = list(find_amicable_pairs(10000))
        self.assertEqual(pairs, expected)

    def test_returns_iterator(self):
        # Should be a lazy iterator, not a list
        result = find_amicable_pairs(100)
        self.assertTrue(hasattr(result, '__next__'))


class TestSumOfAmicableNumbers(unittest.TestCase):
    """Tests for sum_of_amicable_numbers."""

    def test_below_300(self):
        # Only pair is (220, 284) -> sum = 504
        self.assertEqual(sum_of_amicable_numbers(300), 504)

    def test_below_10000(self):
        # (220+284) + (1184+1210) + (2620+2924) + (5020+5564) + (6232+6368)
        expected = 31626
        self.assertEqual(sum_of_amicable_numbers(10000), expected)

    def test_below_1_returns_zero(self):
        self.assertEqual(sum_of_amicable_numbers(1), 0)

    def test_below_2_returns_zero(self):
        self.assertEqual(sum_of_amicable_numbers(2), 0)


if __name__ == "__main__":
    unittest.main()
