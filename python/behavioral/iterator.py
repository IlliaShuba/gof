class Collection:
    def getIterator(self):
        pass


class Iterator:
    def hasNext(self):
        pass

    def next(self):
        pass


class JavaDeveloper(Collection):
    name = None
    skills = None

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSkills(self):
        return self.skills

    def setSkills(self, skills):
        self.skills = skills

    def getIterator(self):
        return SkillIterator()


class SkillIterator(Iterator):
    index = 0

    def hasNext(self):
        if (self.index < len(self.skills)):
            return True
        return False


if __name__ == '__main__':
    skills = ["Java", "Python", "PostgreSQL"]
    javaDeveloper = JavaDeveloper("Illia Shuba", skills)
    iterator = javaDeveloper.getIterator()
    print("Developer: " + javaDeveloper.getName())
    print("Skills: ")
    while (iterator.hasNext()):
        print(str(iterator.next()) + " ", end="")
