from django.urls import path
from . import views
app_name = 'ticketportal'
urlpatterns = [
    path('', views.tickets, name='tickets'),
    path('<int:ticket_id>', views.ticket_detail, name='ticket_detail'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
]