# Generated by Django 3.1.4 on 2021-02-24 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210224_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internattendence',
            old_name='last_reply',
            new_name='date',
        ),
    ]