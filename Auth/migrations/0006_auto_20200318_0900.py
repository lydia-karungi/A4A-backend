# Generated by Django 2.2.2 on 2020-03-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_auto_20200313_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
