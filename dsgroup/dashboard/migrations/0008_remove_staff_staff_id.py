# Generated by Django 3.1.4 on 2021-02-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210226_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='staff_id',
        ),
    ]
