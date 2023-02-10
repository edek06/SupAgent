from django.shortcuts import render
from .models import Ticket
def tickets(request):
    tickets = Ticket.objects
    return render(request, 'ticketportal/tickets.html', {'tickets': tickets})