# Generated by Django 2.2.2 on 2020-03-18 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_auto_20200318_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]