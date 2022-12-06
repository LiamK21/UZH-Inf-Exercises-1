from Exercise8Task5Item import Item
from Exercise8Task5Order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__order_list = []

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list

    def get_order_list(self):
        if len(self.__order_list) == 0:
            return "No order yet"
        valid_order = self.__order_list
        valid_order = Order(valid_order)
        return valid_order

    def set_order(self, item_list):
        for item in item_list:
            if item in self.__menu_list:
                self.__order_list.append(item)
        if len(self.__order_list) == 0:
            return


    def get_revenue(self):
        revenue = Order.get_bill_amount(Order(self.__order_list))
        return revenue


if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]

    # Create order list
    order_list = [steak, salad, fish, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    print(restaurant.get_order_list())
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
