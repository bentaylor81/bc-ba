# Generated by Django 3.0.3 on 2020-02-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_members',
            name='position',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='board_members',
            name='profile',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
