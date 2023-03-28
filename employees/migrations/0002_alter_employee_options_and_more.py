# Generated by Django 4.1.6 on 2023-03-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['name']},
        ),
        migrations.RemoveIndex(
            model_name='employee',
            name='employees_e_joined_20987a_idx',
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['name'], name='employees_e_name_95200c_idx'),
        ),
    ]