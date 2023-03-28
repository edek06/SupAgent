from .models import Ticket
from django import forms
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category', 'priority', 'author', 'status']