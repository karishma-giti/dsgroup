# Generated by Django 3.1.4 on 2021-03-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210301_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internattendance',
            name='attendance',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='1', max_length=100),
        ),
    ]
