from django.shortcuts import render, get_object_or_404
from .models import Ticket
def tickets(request):
    # all tickets save in 'tickets'
    tickets = Ticket.objects.all()
    # show tickets on this page "tickets.html"
    return render(request, 'ticketportal/tickets.html', {'tickets': tickets})

# details of one ticket display
def ticket_detail(request, ticket_id):
    # if ID is valid, save this object in ticket-Variable
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    # return this page and the ticket
    return render(request, 'ticketportal/ticket_detail.html', {'ticket': ticket})
