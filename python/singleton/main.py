from array import array
from builtins import print, type, super

from locale import str
from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DB(metaclass=SingletonMeta):
    db: array = None

    def __init__(self) -> None:
        self.db = []

    def save_user(self, user: str):
        self.db.append(user)

    def delete_user(self, user: str):
        self.db.remove(user)

    def get_all_users(self):
        return self.db


def test_singleton(user: str) -> None:
    DB().save_user(user)
    print(DB().get_all_users())


if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args="Ivan")
    process2 = Thread(target=test_singleton, args="Denis")
    process1.start()
    process2.start()
