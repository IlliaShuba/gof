class User:
    def sendMessage(self, message):
        pass

    def getMessage(self, message):
        pass


class Admin(User):
    chat = None
    name = None

    def __init__(self, chat, name):
        self.chat = chat
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def sendMessage(self, message):
        self.chat.sendMessage(message, self.this)

    def getMessage(self, message):
        print(self.name + " receiving message " + message + ".")


class Chat:
    def sendMessage(self, message, User):
        pass


class SimpleTextChat(Chat):
    admin = None
    users = None

    def setAdmin(self, admin):
        self.admin = admin

    def addUserToChat(self, user):
        def sendMessage(self, message, user):
            for u in self.users:
                if (u != user):
                    u.getMessage(message)
            self.admin.getMessage(message)


class SimpleUser(User):
    chat = None
    name = None

    def __init__(self, chat, name):
        self.chat = chat
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def sendMessage(self, message):
        self.chat.sendMessage(message, self.this)

    def getMessage(self, message):
        print(self.name + " receiving message: " + message + ".")


if __name__ == "__main__":
    chat = SimpleTextChat()
    admin = Admin(chat, "Admin")
    user1 = SimpleUser(chat, "User 1")
    user2 = SimpleUser(chat, "User 2")
    chat.setAdmin(admin)
    chat.addUserToChat(user1)
    chat.addUserToChat(user2)
    user1.sendMessage("Hello, I am user 1!!!")
    admin.sendMessage("Roger that. I am admin!")