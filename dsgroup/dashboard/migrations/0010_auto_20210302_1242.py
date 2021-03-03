# Generated by Django 3.1.2 on 2021-03-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210301_1438'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Salary',
            new_name='Payroll',
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.CharField(blank=True, default='02/03/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='internattendance',
            name='date',
            field=models.CharField(blank=True, default='02/03/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffattendance',
            name='date',
            field=models.CharField(blank=True, default='02/03/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='traineeattendance',
            name='date',
            field=models.CharField(blank=True, default='02/03/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='trainerattendance',
            name='date',
            field=models.CharField(blank=True, default='02/03/2021', max_length=100),
        ),
    ]
