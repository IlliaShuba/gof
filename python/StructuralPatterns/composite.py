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


class Client:
    def __init__(self):
        self.orders = []

    def add_item(self, *args):
        self.orders.extend(args)

    def remove_item(self, *args):
        for item in args:
            self.orders.remove(item)

    def show_order(self):
        print("Show client order...")
        for item in self.orders:
            item.delivery()


if __name__ == '__main__':
    client = Client()
    firstOrder = Letter()
    secondOrder = Parcel()

    client.add_item(firstOrder)
    client.add_item(secondOrder)

    client.show_order()
