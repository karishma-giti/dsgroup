# Generated by Django 3.1.2 on 2021-02-24 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210222_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='graduation_marksheet',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='graduation_percent',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='high_school_marksheet',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='high_school_percent',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='other_marksheet',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='other_percent',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='post_graduation_marksheet',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='post_graduation_percent',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='school_marksheet',
        ),
    ]