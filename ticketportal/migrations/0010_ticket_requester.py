# Generated by Django 4.1.6 on 2023-04-18 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_options_and_more'),
        ('ticketportal', '0009_remove_ticket_respons_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='requester',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
    ]
