from abc import ABC, abstractmethod


class Cargo(ABC):
    def __init__(self, type):
        self._type = type

    @abstractmethod
    def create(self):
        pass


class Office(ABC):

    def __init__(self, type):
        self._type = type

    @abstractmethod
    def create(self):
        pass


class Letter(Cargo):
    def __init__(self):
        super().__init__("Letter")

    def create(self):
        print("Description for letter!")


class SmallOffice(Office):
    def __init__(self):
        super().__init__("Letter")

    def create(self):
        print("Small office processing order!")


class Parcel(Cargo):
    def __init__(self):
        super().__init__("Parcel")

    def create(self):
        print("Description for parcel!")


class LargeOffice(Office):
    def __init__(self):
        super().__init__("Parcel")

    def create(self):
        print("Large office processing order!")


class OrderFactory(ABC):
    @abstractmethod
    def get_cargo(self):
        pass

    @abstractmethod
    def get_office(self):
        pass


class LetterFactory(OrderFactory):
    def get_cargo(self):
        return Letter()

    def get_office(self):
        return SmallOffice()


class ParcelFactory(OrderFactory):
    def get_cargo(self):
        return Parcel()

    def get_office(self):
        return LargeOffice()


class Application:
    def __init__(self, factory: OrderFactory):
        self.__factory = factory

    def get_checkbox(self):
        return self.__factory().get_office().create()

    def get_button(self):
        return self.__factory().get_cargo().create()


if __name__ == "__main__":
    win = Application(LetterFactory)
    win.get_checkbox()
    win.get_button()

    mac = Application(ParcelFactory)
    mac.get_checkbox()
    mac.get_button()