# Generated by Django 4.1.6 on 2023-02-10 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketportal', '0003_alter_ticket_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='closed',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='deadline',
        ),
    ]
