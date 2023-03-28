from django.db import models

# we need this model to create all employees. For this users we can create a Ticket.
# It's not the same like accounts - employees can not be an owner - only an end user
class Employee(models.Model):
    # Name and Surname of this employee
    name = models.CharField(max_length=50)
    # a date, when this user was created
    joined = models.DateTimeField(auto_now_add=True)

    # all Employees will be sort by joined (created) field
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    # return a name of this employee
    def __str__(self):
        return self.name