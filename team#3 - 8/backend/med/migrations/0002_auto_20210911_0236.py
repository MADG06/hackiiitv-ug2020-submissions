# Generated by Django 3.2.5 on 2021-09-10 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetails',
            old_name='cust_name',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='customerdetails',
            name='cust_phone',
        ),
    ]
