# Generated by Django 3.0.3 on 2020-03-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0031_auto_20200328_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta',
            name='meta_keywords',
            field=models.CharField(default='BC-BA', max_length=200),
        ),
    ]
