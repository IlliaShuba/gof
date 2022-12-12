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
                order = Letter()
            elif type == "parcel":
                print("Create parcel...")
                order = Parcel()
        return order


if __name__ == '__main__':
    order_factory = OrderFactory()
    orders = []

    orders.append(order_factory.get_order_by_type("letter"))
    orders.append(order_factory.get_order_by_type("letter"))

    orders.append(order_factory.get_order_by_type("parcel"))
    orders.append(order_factory.get_order_by_type("parcel"))

    for order in orders:
        order.delivery()
