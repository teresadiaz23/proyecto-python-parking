from aplicacion.app import db
from aplicacion.models.ticket import Ticket


class TicketRepositorio():

    def save(self, ticket):
        db.session.add(ticket)
        db.session.commit()


    def find_all(self):
        tickets = Ticket.query.all()
        return tickets


    def find_by_pin(self, pin):
        ticket = Ticket.query.filter_by(pin=pin).first()
        return ticket


    def find_by_matricula(self, matricula):
        ticket = Ticket.query.filter_by(matricula=matricula).first()
        return ticket




ticket_repositorio = TicketRepositorio()
