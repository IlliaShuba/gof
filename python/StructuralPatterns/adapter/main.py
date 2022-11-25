import abc
from abc import ABC

class Database(ABC):
    @abc.abstractmethod
    def insert(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def select(self):
        pass

    @abc.abstractmethod
    def remove(self):
        pass

class PythonAplication:
    def __init__(self):
        pass

    def saveObject(self):
        print('Save')

    def updateObject(self):
        print('Update')

    def loadObject(self):
        print('Load')

    def deleteObject(self):
        print('Delete')

class Adapter(PythonAplication):
    def __init__(self):
        self.aplication = PythonAplication()

    def insert(self):
        self.aplication.saveObject()

    def update(self):
        self.aplication.updateObject()

    def select(self):
        self.aplication.loadObject()

    def remove(self):
        self.aplication.deleteObject()


if __name__ == '__main__':
    database = Adapter()

    database.insert()
    database.update()
    database.select()
    database.remove()