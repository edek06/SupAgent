from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
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