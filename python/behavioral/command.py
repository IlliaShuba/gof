class Command:
    def execute(self):
        pass


class Database:
    def insert(self):
        print("Inserting record...")

    def update(self):
        print("Updating record...")

    def select(self):
        print("Reading record...")

    def delete(self):
        print("Deleting record...")


class DeleteCommand(Command):
    database = None

    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.insert()


class Developer:
    insert = None
    update = None
    select = None
    delete = None

    def __init__(self, insert, update, select, delete):
        self.insert = insert
        self.update = update
        self.select = select
        self.delete = delete

    def insertRecord(self):
        self.insert.execute()

    def updateRecord(self):
        self.update.execute()

    def selectRecord(self):
        self.select.execute()

    def deleteRecord(self):
        self.delete.execute()


class InsertCommand(Command):
    database = None

    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.update()


class SelectCommand(Command):
    database = None

    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.select()


class UpdateCommand(Command):
    database = None

    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.delete()


if __name__ == "__main__":
    database = Database()
    developer = Developer(InsertCommand(database), UpdateCommand(database), SelectCommand(database),
                          DeleteCommand(database))
    developer.insertRecord()
    developer.updateRecord()
    developer.selectRecord()
    developer.deleteRecord()