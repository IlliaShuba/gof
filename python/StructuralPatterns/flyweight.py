from abc import ABC
from abc import abstractmethod


class Order(ABC):

    @abstractmethod
    def delivery(self):
        pass


class Letter(Order):
    def __init__(self):
        pass

    def delivery(self):
        print("Letter delivery...")


class Parcel(Order):
    def __init__(self):
        pass

    def delivery(self):
        print("Parcel delivery...")


class OrderFactory:
    orders = dict()

    @staticmethod
    def get_order_by_type(type):
        order = OrderFactory.orders.get(type)
        if order is None:
            if type == "letter":
                print("Create letter...")
            elif type == "parcel":
                print("Create parcel...")
            OrderFactory.orders[type] = order
        return order


if __name__ == '__main__':
    order_factory = OrderFactory()
    orders = []

    orders.__add__(order_factory.get_order_by_type("letter"))
    orders.__add__(order_factory.get_order_by_type("letter"))

    for order in orders:
        order.delivery()
