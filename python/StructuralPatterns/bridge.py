from abc import ABC, abstractmethod


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


class Office(ABC):
    def __init__(self, order: Order):
        self.order = order

    def processing_order(self):
        pass


class SmallOffice(Office):
    def __init__(self, order: Order):
        super().__init__(order)

    def processing_order(self):
        print("Small office processing order...")
        self.order.delivery()


class LargeOffice(Office):
    def __init__(self, order: Order):
        super().__init__(order)

    def processing_order(self):
        print("Large office processing order...")
        self.order.delivery()


if __name__ == '__main__':
    offices = [SmallOffice(Letter()), LargeOffice(Parcel())]
    for office in offices:
        office.processing_order()
