# Generated by Django 3.0.3 on 2020-03-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('company', models.CharField(default='', max_length=200)),
                ('position', models.CharField(default='', max_length=200)),
                ('address', models.TextField(blank=True)),
                ('zip_code', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('website', models.CharField(default='', max_length=200)),
                ('membership_type', models.CharField(default='', max_length=200)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]