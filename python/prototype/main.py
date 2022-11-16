from copy import deepcopy
from abc import ABC


class Cargo:
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume

    def __str__(self):
        return f"V{self.weight}"


class Order(ABC):
    pass


class Prototype(Order):
    def __init__(self, cargo: Cargo, price, description):
        self.price = price
        self.cargo = cargo
        self.description = description

    def __str__(self):
        return f"prototype "


if __name__ == "__main__":
    order1 = Prototype(Cargo(3.5, 4), 5, "some")
    order2 = deepcopy(order1)
    order2.price = 10
    order2.cargo.weight = 5.0
    print(order1)
    print(order2)
