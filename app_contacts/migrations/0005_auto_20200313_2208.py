# Generated by Django 3.0.3 on 2020-03-13 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_contacts', '0004_remove_contact_date_edited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
