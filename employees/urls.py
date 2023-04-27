from django.urls import path
from . import views
app_name = 'employees'
urlpatterns = [
    path('', views.show_employees, name='employees'),
    path('add_employee', views.add_employee, name='add_employee'),
]