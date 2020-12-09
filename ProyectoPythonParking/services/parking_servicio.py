class ParkingServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, parking):
        self.repositorio.save(parking)

    def findAll(self):
        return self.repositorio.findAll()

