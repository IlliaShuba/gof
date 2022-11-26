class Order:
    def __init__(self):
        self.is_delivered = False

    def start(self):
        print("Order is active.")
        self.is_delivered = False

    def finish(self):
        print("Order is not active.")
        self.is_delivered = True


class Courier:
    def deliver(self, order: Order):
        if order.is_delivered:
            print("The courier delivered the order!")
        else:
            print("The courier delivers the order...")


class Worker:
    def packing(self):
        print("Packing...")


class Workflow:
    def __init__(self):
        self.worker = Worker()
        self.courier = Courier()
        self.order = Order()

    def process(self):
        self.worker.packing()
        self.order.start()
        self.courier.deliver(self.order)


if __name__ == '__main__':
    workflow = Workflow()
    workflow.process()
