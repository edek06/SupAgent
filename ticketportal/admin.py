from django.contrib import admin
from .models import Ticket
# it's this same like 'admin.site.register(Ticket)' - model Ticket registrieren für Admin-Page
@admin.register(Ticket)
#now we can self change this look! (127.0.0.1:8000/admin)
class TicketAdmin(admin.ModelAdmin):
    # this parameter will be display
    list_display = ['id', 'title', 'respons_user', 'author', 'created', 'status', 'category', 'priority']
    # we can filter all posts
    list_filter = ['id', 'title', 'respons_user', 'author', 'created', 'status', 'category', 'priority']
    # this will be can find
    search_fields = ['title']
    date_hierarchy = 'created'
    ordering = ['created']