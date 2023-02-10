from django.shortcuts import render
from .models import Ticket
def tickets(request):
    tickets = Ticket.all()
    return render(request, 'ticketportal/ticketportal/tickets.html', {'tickets': tickets})