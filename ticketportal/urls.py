from django.urls import path
from . import views
app_name = 'ticketportal'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tickets/', views.tickets, name='tickets'),
    path('tck/<str:category>/', views.tck, name='tck'),
    path('closed/', views.closed, name='closed'),
    path('<int:ticket_id>', views.ticket_detail, name='ticket_detail'),
    path('<int:ticket_id>/close/', views.close_ticket, name='close_ticket'),
    path('<int:ticket_id>/edit_ticket/', views.edit_ticket, name='edit_ticket'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('employee_tickets/<int:employee_id>', views.show_employee_tickets, name='employee_tickets'),
]