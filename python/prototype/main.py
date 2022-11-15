from copy import deepcopy, copy
from abc import ABC, abstractmethod


class Cargo:
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume

    def __str__(self):
        return f"V{self.weight}"


class Order(ABC):
    @abstractmethod
    def ride(self):
        pass

class Prototype(Order):
    def __init__(self, price, cargo: Cargo, description):
        self.price = price
        self.cargo = cargo
        self.description = description

    def __str__(self):
        return f"prototype "


if __name__ == "__main__":
    order1 = Prototype(Cargo(3.5, 4), 5)
    order2 = deepcopy(order1)
    order2.price = "R8"
    order2.cargo.weight = 5.0
    print(order1)
    print(order2)
