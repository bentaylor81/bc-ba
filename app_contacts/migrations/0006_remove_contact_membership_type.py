# Generated by Django 3.0.3 on 2020-03-13 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_contacts', '0005_auto_20200313_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='membership_type',
        ),
    ]
