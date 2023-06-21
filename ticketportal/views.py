from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm, TicketCloseForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from employees.models import Employee

@login_required(login_url="/")
def dashboard(request):
    all_tickets = Ticket.objects.all()
    activ_tickets = Ticket.objects.filter(status='ACT')
    closed_tickets = Ticket.objects.filter(status='CSD')
    all_incidents = Ticket.objects.filter(category='INC', status='ACT')
    return render(request, 'ticketportal/dashboard.html', {'all_tickets':all_tickets,
                                                           'activ_tickets':activ_tickets,
                                                           'closed_tickets':closed_tickets,
                                                           'all_incidents':all_incidents})
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
def tck(request, category):
    # all tickets from user
    all_tickets = Ticket.objects.filter(category=category, status='ACT')
    # first 20 employess on the page
    paginator = Paginator(all_tickets, 12)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)
    # it will be sent an information, what category of ticket it is (in Text) ... 's' for plural
    str_category = Ticket.Category(category).label + 's'
    # show tickets on this page "tck.html"
    return render(request, 'ticketportal/tck.html', {'tickets': tickets, 'category':str_category})

@login_required(login_url="/")
def closed(request):
    # all closed tickets
    closed_tickets = Ticket.objects.filter(status='CSD')
    # first 16 tickets on the page
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

@login_required(login_url="/")
def show_employee_tickets(request, employee_id):
    # all tickets of this employee sort by ID
    employee_tickets = Ticket.objects.filter(requester=employee_id).order_by('-id')
    # name of employee als object
    employee = get_object_or_404(Employee, pk=employee_id)
    # first 20 employess on the page
    paginator = Paginator(employee_tickets, 16)
    # beginn with the first page
    page_number = request.GET.get('page', 1)
    # save all this infomations in the variable
    tickets = paginator.page(page_number)

    return render(request, 'ticketportal/employee_tickets.html', {'tickets': tickets, 'employee':employee})