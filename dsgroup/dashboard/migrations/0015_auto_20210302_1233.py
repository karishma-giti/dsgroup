# Generated by Django 3.1.4 on 2021-03-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20210302_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffattendance',
            name='attendance',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
