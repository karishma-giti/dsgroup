# Generated by Django 3.1.4 on 2021-02-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20210224_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internattendance',
            name='date',
            field=models.DateField(blank=True, default='24/02/2021'),
        ),
    ]
