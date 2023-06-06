from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm, TicketCloseForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone

@login_required(login_url="/")
def tickets(request):
    # all tickets save in 'tickets'
    activ_tickets = Ticket.objects.filter(status='ACT')
    #first 20 employess on the page
    paginator = Paginator(activ_tickets, 15)
    #beginn with the first page
    page_number = request.GET.get('page', 1)
    #save all this infomations in the variable
    tickets = paginator.page(page_number)
    # show tickets on this page "tickets.html"
    return render(request, 'ticketportal/tickets.html', {'tickets': tickets})

@login_required(login_url="/")
def tck(request):
    # all tickets from user
    all_tickets = Ticket.objects.filter(category='TCK', status='ACT')
    # first 20 employess on the page
    paginator = Paginator(all_tickets, 12)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)
    # show tickets on this page "tck.html"
    return render(request, 'ticketportal/tck.html', {'tickets': tickets})

@login_required(login_url="/")
def inc(request):
    # all incidents from user
    all_incidents = Ticket.objects.filter(category='INC', status='ACT')
    # first 20 employess on the page
    paginator = Paginator(all_incidents, 12)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)
    # show tickets on this page "inc.html"
    return render(request, 'ticketportal/inc.html', {'tickets': tickets})

@login_required(login_url="/")
def srq(request):
    # all service requests from user
    all_requests = Ticket.objects.filter(category='SRQ', status='ACT')
    # first 20 employess on the page
    paginator = Paginator(all_requests, 12)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)
    # show tickets on this page "srq.html"
    return render(request, 'ticketportal/srq.html', {'tickets': tickets})

@login_required(login_url="/")
def chg(request):
    # all changes from user
    all_changes = Ticket.objects.filter(category='CHG', status='ACT')
    # first 20 employess on the page
    paginator = Paginator(all_changes, 12)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)
    # show tickets on this page "chg.html"
    return render(request, 'ticketportal/chg.html', {'tickets': tickets})

@login_required(login_url="/")
def closed(request):
    # all closed tickets
    closed_tickets = Ticket.objects.filter(status='CSD')
    # first 20 employess on the page
    paginator = Paginator(closed_tickets, 16)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)
    # show tickets on this page "closed.html"
    return render(request, 'ticketportal/closed.html', {'tickets': tickets})

# details of one ticket display
@login_required(login_url="/")
def ticket_detail(request, ticket_id):
    # if ID is valid, save this object in ticket-Variable
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    # return this page and the ticket
    return render(request, 'ticketportal/ticket_detail.html', {'ticket': ticket})

@login_required(login_url="/")
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

# ticket will closed - STATUS will changed from "Active" to "Closed"
@login_required(login_url="/")
def close_ticket(request, ticket_id):
    # if ID is valid, save this object in ticket-Variable
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    # check aktually status
    if ticket.status == Ticket.Status.CLOSED:
        info = "Ticket already closed. No action needed."
        # And back to the Homepage
        return render(request, 'ticketportal/close.html', {'info': info})
    if request.method == 'POST':
        # create a form instance and fill in with a ticket-details
        form = TicketCloseForm(request.POST, instance=ticket)
        # check whether it's valid:
        if form.is_valid():
            # change a value of status to 'Closed'
            ticket.status = Ticket.Status.CLOSED
            # set a time
            ticket.closed = timezone.now()
            # Save the comment to the database
            ticket.save()
            info = "Ticket closed successfully"
            return render(request, 'ticketportal/close.html', {'info':info})
    else:
        form = TicketCloseForm(instance=ticket)
        # And back to the Homepage
        return render(request, 'ticketportal/close.html', {'ticket': ticket, 'form':form})

@login_required(login_url="/")
def close_ticket_backup(request, ticket_id):
    # if ID is valid, save this object in ticket-Variable
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    # check aktually status
    if not ticket.status == Ticket.Status.CLOSED:
        # change a value for status to 'Closed'
        ticket.status = Ticket.Status.CLOSED
        # turn the info back
        info = "Ticket closed successfully"
    else:
        info = "Ticket already closed. No action needed."
    # Save the comment to the database
    ticket.save()
    # And back to the Homepage
    return render(request, 'ticketportal/close.html', {'info':info})

@login_required(login_url="/")
def edit_ticket(request, ticket_id):
    # if ID is valid, save this object in ticket-Variable
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and fill in with a ticket-details
        form = TicketForm(request.POST, instance=ticket)
        # check whether it's valid:
        if form.is_valid():
            # Save the comment to the database
            ticket.save()
            # And back to the Homepage
            return redirect('ticketportal:tickets')
    else:
        # current ticket in a form saving
        form = TicketForm(instance=ticket)
        # return this page and the ticket
        return render(request, 'ticketportal/edit_ticket.html', {'ticket': ticket, 'form':form})