from django.shortcuts import render
from .models import Ticket
def tickets(request):
    # all tickets save in 'tickets'
    tickets = Ticket.objects
    # show tickets on this page "tickets.html"
    return render(request, 'ticketportal/tickets.html', {'tickets': tickets})