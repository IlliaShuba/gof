from abc import ABC, abstractmethod


class Project(ABC):
    @abstractmethod
    def run(self):
        pass


class ProxyProject(Project):
    url = None
    realProject = None

    def __init__(self, url):
        self.url = url

    def run(self):
        if self.realProject is None:
            self.realProject = RealProject(self.url)
        self.realProject.run()


class RealProject(Project):
    url = None

    def __init__(self, url):
        self.url = url
        self.load()

    def load(self):
        print("Loading project from" + self.url + "...")

    def run(self):
        print("Running project" + self.url + "...")


if __name__ == '__main__':
    project = ProxyProject("https://www.github.com/erere/realProject")
    project.run()
