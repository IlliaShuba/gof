class Order:
    def __init__(self, description, price):
        self.description = description
        self.price = price
        self._status = "Ready"

    def startProcessing(self):
        self._status = "Running"
    def finish(self):
        self._status = "Ready"
    def is_ready(self):
        return self._status == "Ready"

class OrderPool:
    def __init__(self):
        pass

    _pool = [Order("some description 1", 100), Order("some description 2", 200)]

    def _is_free(self, meeting):
        return meeting.is_ready()

    def get_order(self) -> Order:
        free_order = list(filter(self._is_free, OrderPool._pool))
        if free_order:
            order = free_order[0]
            order.startProcessing()
            print(order.description)
            return order
        else:
            print("No free order")

    def release_order(self, order):
        order.finish()
        print("finish order")


if __name__ == '__main__':
    pool = OrderPool()
    order1 = pool.get_order()
    order2 = pool.get_order()
    order3 = pool.get_order()
    pool.release_order(order1)