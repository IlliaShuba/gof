from abc import ABC, abstractmethod


class Order(ABC):

    @abstractmethod
    def delivery(self):
        pass


class QuickOrder(Order):
    def __init__(self):
        pass

    def delivery(self):
        print("Delivery quick order ")


class OrderDecorator(Order):
    def __init__(self, order: Order):
        self.order = order

    def delivery(self):
        self.delivery()


class Letter(OrderDecorator):

    def __init__(self, order: Order):
        super().__init__(order)

    @staticmethod
    def show_info() -> str:
        return "Letter"

    def delivery(self):
        super(self).delivery()
        print(self.show_info())

class Parcel(OrderDecorator):

    def __init__(self, order: Order):
        super().__init__(order)

    @staticmethod
    def show_description() -> str:
        return "Parcel"

    def delivery(self):
        super(self).delivery()
        print(self.show_description())


if __name__ == '__main__':
    order = Parcel(QuickOrder())
    order.delivery()