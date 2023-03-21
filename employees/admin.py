from django.contrib import admin
from .models import Employee
# it's the same like 'admin.site.register(Employee)' - model Ticket registrieren für Admin-Page
@admin.register(Employee)
#now we can self change this look! (127.0.0.1:8000/admin)
class EmployeeAdmin(admin.ModelAdmin):
    # this parameter will be display
    list_display = ['id', 'name', 'joined']
    # we can filter all posts
    list_filter = ['id', 'name', 'joined']
    # this will be can find
    search_fields = ['name']
    date_hierarchy = 'joined'
    ordering = ['joined']