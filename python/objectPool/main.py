class Order:
    def __init__(self, order_type, description, price):
        self.order_type = order_type
        self.description = description
        self.price = price
        self._status = "Running"

    def is_ready(self):
        return self._status == "Ready"

    def update_title(self, title):
        self._title = title


class OrderPool:
    def __init__(self):
        pass

    _pool = [Order(1, "ZOOM", ""), Order(2, "HANGOUTS", "")]

    def _is_free(self, meeting):
        return meeting.is_ready()

    def start_meeting_for(self, title) -> Order:
        freeMeetings = list(filter(self._is_free, OrderPool._pool))
        if freeMeetings:
            meeting = freeMeetings[0]
            meeting.update_title(title)
            meeting.start_meeting()
            return meeting
        else:
            print("No free meetings")

    def release_meeting(self, meeting):
        meeting.finish_meeting()


if __name__ == '__main__':
    pool = OrderPool()
    algebra = pool.start_meeting_for("Algebra")
    algebra2 = pool.start_meeting_for("Algebra2")
    pool.release_meeting(algebra2)
    algebra3 = pool.start_meeting_for("Algebra3")