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
    ticket = get_object_or_404(Ticket, id=ticket_id)
    # this page und a ticket return
    return render(request, 'ticketportal/ticket_detail.html', {'ticket': ticket})