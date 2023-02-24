from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
def tickets(request):
    # all tickets save in 'tickets'
    tickets = Ticket.objects.all()
    # show tickets on this page "tickets.html"
    return render(request, 'ticketportal/tickets.html', {'tickets': tickets})

def tck(request):
    # all tickets from user
    tickets = Ticket.objects.filter(category='TCK')
    # show tickets on this page "tck.html"
    return render(request, 'ticketportal/tck.html', {'tickets': tickets})

def inc(request):
    # all incidents from user
    tickets = Ticket.objects.filter(category='INC')
    # show tickets on this page "inc.html"
    return render(request, 'ticketportal/inc.html', {'tickets': tickets})

def srq(request):
    # all service requests from user
    tickets = Ticket.objects.filter(category='SRQ')
    # show tickets on this page "srq.html"
    return render(request, 'ticketportal/srq.html', {'tickets': tickets})

def chg(request):
    # all changes from user
    tickets = Ticket.objects.filter(category='CHG')
    # show tickets on this page "chg.html"
    return render(request, 'ticketportal/chg.html', {'tickets': tickets})

def closed(request):
    # all closed tickets
    tickets = Ticket.objects.filter(status='CSD')
    # show tickets on this page "closed.html"
    return render(request, 'ticketportal/closed.html', {'tickets': tickets})

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
            # And back to the Homepage
            return redirect('ticketportal:tickets')
    # if a GET we'll create a blank form
    else:
        form = TicketForm()
        return render(request, 'ticketportal/create_ticket.html',
                      {'form': form})