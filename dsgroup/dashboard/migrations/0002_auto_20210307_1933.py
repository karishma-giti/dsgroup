# Generated by Django 3.1.2 on 2021-03-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.CharField(blank=True, default='07/03/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='internattendance',
            name='date',
            field=models.CharField(blank=True, default='07-03-2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffattendance',
            name='date',
            field=models.CharField(blank=True, default='07/03/2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='traineeattendance',
            name='date',
            field=models.CharField(blank=True, default='07-03-2021', max_length=100),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='position',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainerattendance',
            name='date',
            field=models.CharField(blank=True, default='07-03-2021', max_length=100),
        ),
    ]
