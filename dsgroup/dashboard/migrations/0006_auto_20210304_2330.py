# Generated by Django 3.1.2 on 2021-03-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210304_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
