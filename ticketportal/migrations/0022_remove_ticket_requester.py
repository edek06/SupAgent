# Generated by Django 4.1.6 on 2023-04-24 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketportal', '0021_ticket_requester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='requester',
        ),
    ]
