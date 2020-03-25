# Generated by Django 3.0.3 on 2020-03-08 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0017_auto_20200308_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_members',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board_members',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pages',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
