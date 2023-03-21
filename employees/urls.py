from django.urls import path
from . import views
app_name = 'employees'
urlpatterns = [
    path('', views.show_employees, name='employees'),
]