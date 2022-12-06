#!/usr/bin/env python3

from unittest import TestCase
from Exercise8Task5 import Restaurant
from Exercise8Task5Item import Item


class PublicTestSuite(TestCase):
    def test_get_revenue(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [steak, salad, fish]
        # Create order list
        order_list = [steak, steak, salad, pizza]
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 60
        # Assertion
        self.assertEqual(actual, expected)

    def test_no_order(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [steak, salad, fish]
        # Create order list
        order_list = []
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_order_list()
        # Expected return
        expected = "No order yet"
        # Assertion
        self.assertEqual(expected, actual)

    def test_order_doesnt_match(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [pizza]
        # Create order list
        order_list = [steak, salad]
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_order_list()
        # Expected return
        expected = restaurant.get_revenue()
        # Assertion
        self.assertEqual(expected, actual)


