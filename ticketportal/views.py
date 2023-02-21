from django.shortcuts import render, get_object_or_404
from .models import Ticket
from .forms import TicketForm
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

def create_ticket(request):
    ticket = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TicketForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Create a Ticket object without saving it to the database
            ticket = form.save(commit=False)
            # Save the comment to the database
            ticket.save()
    # if a GET we'll create a blank form
    else:
        form = TicketForm()
    return render(request, 'ticketportal/create_ticket.html',
                  {'form': form,
                   'ticket': ticket})