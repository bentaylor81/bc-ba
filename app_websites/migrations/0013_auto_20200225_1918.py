# Generated by Django 3.0.3 on 2020-02-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0012_auto_20200225_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_members',
            name='profile',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
