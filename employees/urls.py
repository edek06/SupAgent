from django.urls import path
from . import views
app_name = 'ticketportal'
urlpatterns = [
    path('', views.show_employees, name='employees'),
]