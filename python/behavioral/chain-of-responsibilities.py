class Priority:
    ROUTINE = 1
    IMPORTANT = 2
    ASAP = 3


class Notifier:
    priority = 0
    nextNotifier = None

    def __init__(self, priority):
        self.priority = priority

    def setNextNotifier(self, nextNotifier):
        self.nextNotifier = nextNotifier

    def notifyManager(self, message, level):
        if level >= self.priority:
            self.write(message)
        if self.nextNotifier is not None:
            self.nextNotifier.notifyManager(message, level)

    def write(self, message):
        pass


class EmailNotifier(Notifier):
    def __init__(self, priority):
        super().__init__(priority)

    def write(self, message):
        print("Sending email: " + message)


class SimpleReportNotifier(Notifier):
    def __init__(self, priority):
        super().__init__(priority)

    def write(self, message):
        print("Notifying using simple report: " + message)


class SMSNotifier(Notifier):
    def __init__(self, priority):
        super().__init__(priority)

    def write(self, message):
        print("Sending SMS to manager:" + message)


if __name__ == '__main__':
    reportNotifier = SimpleReportNotifier(Priority.ROUTINE)
    emailNotifier = EmailNotifier(Priority.IMPORTANT)
    smsNotifier = SMSNotifier(Priority.ASAP)
    reportNotifier.setNextNotifier(emailNotifier)
    emailNotifier.setNextNotifier(smsNotifier)
    reportNotifier.notifyManager("Everything is OK.", Priority.ROUTINE)
    reportNotifier.notifyManager("Something went wrong!", Priority.IMPORTANT)
    reportNotifier.notifyManager("Houston, we`ve had a problem here!!!", Priority.ASAP)
