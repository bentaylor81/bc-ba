# Generated by Django 3.0.3 on 2020-02-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board_members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(default='', max_length=200)),
                ('profile', models.CharField(default='', max_length=200)),
                ('linkedin', models.CharField(default='', max_length=200)),
                ('image_url', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
