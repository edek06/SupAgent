from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.contrib.auth.decorators import login_required

def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employees.html', {'employees':employees})