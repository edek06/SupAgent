from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def show_employees(request):
    return render(request, 'employees/employees.html')