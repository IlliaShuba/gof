class Collection:
    def getIterator(self):
        pass


class Iterator:
    def hasNext(self):
        pass

    def next(self):
        pass


class PythonDeveloper(Collection):
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
        return SkillIterator(skills)


class SkillIterator(Iterator):
    index = 0
    skills = None

    def __init__(self, skills):
        self.skills = skills

    def next(self):
        if self.index < len(self.skills):
            skill = self.skills[self.index]
            self.index += 1
            return skill
        self.index += 1

    def hasNext(self):
        if (self.index < len(self.skills)):
            return True
        return False


if __name__ == '__main__':
    skills = ["Java", "Python", "PostgreSQL"]
    pythonDeveloper = PythonDeveloper("Illia Shuba", skills)
    iterator = pythonDeveloper.getIterator()
    print("Developer: " + pythonDeveloper.getName())
    print("Skills: ")
    while iterator.hasNext():
        print(str(iterator.next()) + " ", end="")
