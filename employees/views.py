from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url="/")
def show_employees(request):
    #save all employees in variable
    list_employees = Employee.objects.all()
    #first 20 employess on the page
    paginator = Paginator(list_employees, 20)
    #beginn with the first page
    page_number = request.GET.get('page', 1)
    #save all this infomations in the variable
    employees = paginator.page(page_number)
    return render(request, 'employees/employees.html', {'employees':employees})

@login_required(login_url="/")
def add_employee(request):
    message = ""
    employee = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Create an Employee object without saving it to the database
            employee = form.save(commit=False)
            # Check or Employee exists already
            if not check_employee(employee.name):
                # Save the comment to the database
                employee.save()
                # And back to the Employees
                return redirect('employees:employees')
            else:
                message = "Employee already exists"
                return render(request, 'employees/add_employee.html',
                              {'form': form, 'message': message})
    # if a GET we'll create a blank form
    else:
        form = EmployeeForm()
        return render(request, 'employees/add_employee.html',
                      {'form': form,'message':message})

def check_employee(new_employee):
    exist = False
    employees = Employee.objects.all()
    for employee in employees:
        if new_employee == employee.name:
            exist = True
    return exist