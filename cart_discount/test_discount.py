import unittest
from unittest import TestCase
from price_discount import discount

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))


    def test_list_of_two_prices(self):
        prices = [10, 20]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))


    def test_equal_prices(self):
        prices = [10, 10, 10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))


    def test_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))


if __name__ == '__main__':
    unittest.main()
