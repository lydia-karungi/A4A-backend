# Generated by Django 2.2.2 on 2020-03-31 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0016_auto_20200327_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='user',
            new_name='profile',
        ),
    ]
