# Generated by Django 3.0.3 on 2020-03-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_websites', '0028_auto_20200328_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='meta_page',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='meta',
            name='meta_description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='meta',
            name='meta_keywords',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='meta',
            name='meta_title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
