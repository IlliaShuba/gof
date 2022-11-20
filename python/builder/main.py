from abc import ABC, abstractmethod
from enum import Enum


class Type(Enum):
    Letter = "Letter"
    Parcel = "Parcel"


class Order:
    def __init__(self):
        self.type = None
        self.description = None
        self.price = None

    def __str__(self):
        return f"Order type={self.type.name}, description={self.description}, price={self.price}"


class OrderBuilder(ABC):
    @abstractmethod
    def set_type(self) -> None:
        pass

    @abstractmethod
    def set_description(self) -> None:
        pass

    @abstractmethod
    def set_price(self) -> None:
        pass

    @abstractmethod
    def get_order(self) -> Order:
        return order


class LetterBuilder(OrderBuilder):
    def __init__(self):
        self.order = Order()

    def set_type(self) -> None:
        self.order.type = Type.Letter

    def set_description(self) -> None:
        self.order.description = "some description for letter"

    def set_price(self) -> None:
        self.order.price = 10

    def get_order(self) -> Order:
        return self.order


class ParcelBuilder(OrderBuilder):
    def __init__(self):
        self.order = Order()

    def set_type(self) -> None:
        self.order.type = Type.Letter

    def set_description(self) -> None:
        self.order.description = "some description for parcel"

    def set_price(self) -> None:
        self.order.price = 100

    def get_order(self) -> Order:
        return self.order


class Director:
    def __init__(self, builder: OrderBuilder):
        self.builder = builder

    def create_order(self):
        self.builder.set_description()
        self.builder.set_type()
        self.builder.set_price()

        return self.builder.get_order()


if __name__ == "__main__":
    builder1 = LetterBuilder()
    director = Director(builder1)
    order = director.create_order()
    print(order)
