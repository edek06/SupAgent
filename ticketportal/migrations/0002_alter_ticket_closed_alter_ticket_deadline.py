# Generated by Django 4.1.6 on 2023-02-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closed',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='deadline',
            field=models.DateTimeField(blank=True),
        ),
    ]
