from enum import Enum


class OrderType(Enum):
    LETTER = 0,
    DOCUMENTS = 1,
    PARCEL = 2


class Order:

    def __init__(self, price: float):
        self.__price = price

    def get_price(self):
        return self.__price


class Letter(Order):
    def __init__(self):
        super().__init__(2.0)


class Documents(Order):
    def __init__(self):
        super().__init__(10.0)


class Parcel(Order):
    def __init__(self):
        super().__init__(50.0)


class OrderFactory:

    @staticmethod
    def create(order_type: OrderType) -> Order:
        order_dict = {
            OrderType.LETTER: Letter,
            OrderType.DOCUMENTS: Documents,
            OrderType.PARCEL: Parcel
        }

        return order_dict[order_type]()


if __name__ == "__main__":
    for order in OrderType:
        new_order = OrderFactory.create(order)
        print(f'New order is {order.name} and its price is {new_order.get_price()}')