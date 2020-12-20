from repositories.ticket_repositorio import ticket_repositorio


class TicketServicio():
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repositorio(self):
        return self.__repo

    @repositorio.setter
    def repositorio(self, repo):
        self.__repo = repo

    def save(self, ticket):
        self.repositorio.save(ticket)

    def edit(self, ticket):
        self.repositorio.save(ticket)

    def find_all(self):
        return self.repositorio.find_all()

    def find_by_pin(self, pin):
        return self.repositorio.find_by_pin(pin)

    def find_by_matricula(self, matricula):
        return self.repositorio.find_by_matricula(matricula)


ticket_servicio = TicketServicio(ticket_repositorio)
