# Generated by Django 3.1.2 on 2021-02-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20, null=True, unique=True)),
                ('Profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('emp_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('pan_card', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('percent', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.IntegerField(blank=True, null=True)),
                ('school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.IntegerField(blank=True, null=True)),
                ('high_school_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('post_graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_year', models.IntegerField(blank=True, null=True)),
                ('post_graduation_percent', models.CharField(max_length=100)),
                ('post_graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.IntegerField(blank=True, null=True)),
                ('other_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('other_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('skill', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('gotdetail', models.CharField(blank=True, max_length=100, null=True)),
                ('relationships', models.CharField(blank=True, max_length=100, null=True)),
                ('belongs_department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_id', models.CharField(max_length=20, unique=True)),
                ('Profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('intern_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('pan_card', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.IntegerField(blank=True, null=True)),
                ('school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.IntegerField(blank=True, null=True)),
                ('high_school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('post_graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_year', models.IntegerField(blank=True, null=True)),
                ('post_graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.IntegerField(blank=True, null=True)),
                ('other_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=20, null=True, unique=True)),
                ('staff_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.IntegerField(blank=True, null=True)),
                ('role', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainee_id', models.CharField(max_length=20, unique=True)),
                ('Profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('trainee_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('pan_card', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('percent', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.IntegerField()),
                ('school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.IntegerField(blank=True, null=True)),
                ('high_school_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('post_graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_year', models.IntegerField(blank=True, null=True)),
                ('post_graduation_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.IntegerField(blank=True, null=True)),
                ('other_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('other_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trainer_id', models.CharField(max_length=20, null=True, unique=True)),
                ('Profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Trainer_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('pan_card', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('percent', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.IntegerField(blank=True, null=True)),
                ('school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.IntegerField(blank=True, null=True)),
                ('high_school_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('post_graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_year', models.IntegerField(blank=True, null=True)),
                ('post_graduation_percent', models.CharField(max_length=100)),
                ('post_graduation_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.IntegerField(blank=True, null=True)),
                ('other_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('other_marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('skill', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('gotdetail', models.CharField(blank=True, max_length=100, null=True)),
                ('relationships', models.CharField(blank=True, max_length=100, null=True)),
                ('belongs_department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
