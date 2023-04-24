# Generated by Django 4.1.6 on 2023-04-18 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_options_and_more'),
        ('ticketportal', '0018_alter_ticket_requester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='requester',
            field=models.ForeignKey(default='Grzegorz Wozniak', on_delete=django.db.models.deletion.CASCADE, related_name='tickets_req', to='employees.employee'),
        ),
    ]