#create a models
from django.db import models
#fot time
from django.utils import timezone
#for User Authentication
from django.contrib.auth.models import User
#Model 'Ticket'
class Ticket(models.Model):
    # add a status field of this post
    class Status(models.TextChoices):
        ACTIV = 'ACT', 'Activ'
        CLOSED = 'CSD', 'Closed'
    # add a category of this Ticket
    class Category(models.TextChoices):
        TICKET = 'TCK', 'Ticket'
        INCIDENT = 'INC', 'Incident'
        SERVICE_REQUEST = 'SRQ', 'Service Request'
        CHANGE = 'CHG', 'Change'

    # add a priority field of this post
    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        MIDDLE = 2, 'Middle'
        HIGH = 3, 'High'
    # Main title
    title = models.CharField(max_length=250)
    # Author des tickets
    # CASCADE - what will happend, when one User will delete
    # RELATED_NAME - is a relationship between User and Ticket
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='tickets_aut',
                               default="gwedi")
    # responsible user for this ticket
    #respons_user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                                    blank=True,
    #                                    default="")
    # 
    #respons_user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                                    blank=True,
    #                                    default="")
    # details of this ticket
    description = models.TextField()
    # when this ticket was closed
    #closed = models.DateTimeField(blank=True, default=)
    # when this ticket was created
    created = models.DateTimeField(auto_now_add=True)
    # deadline for this ticket - this parameter will be optional
    #deadline = models.DateTimeField(blank=True)
    # status of this ticket (Aktiv, Done)
    status = models.CharField(max_length=3,
                                choices=Status.choices,
                                default=Status.ACTIV)
    category = models.CharField(max_length=3,
                                choices=Category.choices,
                                default=Category.TICKET)
    priority = models.IntegerField(choices=Priority.choices,
                              default=Priority.LOW)

    # all Tickets will be sort by created field
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    # return a name of post
    def __str__(self):
        return self.title