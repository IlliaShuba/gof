import time


class GithudRepo:
    save = None

    def getSave(self):
        return self.save

    def setSave(self, save):
        self.save = save


class Save:
    version = None

    def __init__(self, version):
        self.version = version

    def getVersion(self):
        return self.version


class Project:
    version = None

    def setVersionAndDate(self, version):
        self.version = version

    def save(self):
        return Save(self.version)

    def load(self, save):
        self.version = save.getVersion()

    def __str__(self):
        return "Project:\n" + "\nVersion: " + self.version + "\n"


if __name__ == "__main__":
    project = Project()
    github = GithudRepo()
    print("Creating new project. Version  1.0")
    project.setVersionAndDate("Version 1.0")
    print("Saving current version to GitHub...")
    github.setSave(project.save())
    print("updating project to version 1.1")
    print("Write poor code...")
    time.sleep(5)
    project.setVersionAndDate("Version 1.1")
    print(project)
    print("Something went wrong...")
    print("Rolling back to version 1.0")
    project.load(github.getSave())
    print("Project after rollback.")
    print(project)