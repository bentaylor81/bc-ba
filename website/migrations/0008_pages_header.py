# Generated by Django 3.0.3 on 2020-02-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200222_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='header',
            field=models.CharField(default='', max_length=200),
        ),
    ]
