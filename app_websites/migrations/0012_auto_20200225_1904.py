# Generated by Django 3.0.3 on 2020-02-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0011_auto_20200225_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_members',
            name='profile',
            field=models.CharField(default='', max_length=200),
        ),
    ]
