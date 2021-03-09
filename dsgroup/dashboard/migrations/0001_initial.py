# Generated by Django 3.1.2 on 2021-03-09 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('emp_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('pan_card', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(default=True, max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(default=True, max_length=100)),
                ('state', models.CharField(default=True, max_length=100)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('address', models.CharField(default=True, max_length=100)),
                ('join_date', models.CharField(default=True, max_length=100)),
                ('document_zip', models.FileField(blank=True, null=True, upload_to='media/')),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('high_school_name', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('high_school_passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('graduation_univercity', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('post_graduation_degree', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('post_graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('other_degree', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('other_univercity', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('other_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('skill', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('position', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=100, null=True)),
                ('experience', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('contact_no', models.IntegerField(blank=True, default=True, null=True)),
                ('emails', models.EmailField(blank=True, default=True, max_length=100, null=True)),
                ('refference', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('relationships', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('belongs_department', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('joining_date', models.CharField(default=True, max_length=100)),
                ('living_date', models.CharField(default=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('intern_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('pan_card', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Asom (Assam)', 'Asom (Assam)'), ('Bihar', 'Bihar'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Chhattisgarh', 'Chhattisgarh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('West Bengal', 'West Bengal'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand (Uttaranchal)', 'Uttarakhand (Uttaranchal)')], max_length=100, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(blank=True, max_length=100, null=True)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('document_zip', models.FileField(blank=True, null=True, upload_to='media/')),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('post_graduation_degree', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('post_graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('regarding', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('reference', models.CharField(choices=[('facebook', 'facebook'), ('instagram', 'instagram'), ('linkain', 'linkain'), ('twitter', 'twitter'), ('other', 'other'), ('people', 'people')], max_length=100, null=True)),
                ('message', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('call', models.CharField(blank=True, default=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, default=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=20, null=True, unique=True)),
                ('staff_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('role', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('trainee_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('pan_card', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
                ('document_zip', models.FileField(blank=True, null=True, upload_to='media/')),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('post_graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(blank=True, null=True, upload_to='media/')),
                ('trainer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('aadhar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('pan_card', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_no', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('address', models.CharField(max_length=100)),
                ('join_date', models.CharField(blank=True, max_length=100, null=True)),
                ('document_zip', models.FileField(blank=True, null=True, upload_to='media/')),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board', models.CharField(blank=True, max_length=100, null=True)),
                ('passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('high_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_board', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_passing_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('post_graduation_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('post_graduation_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('other_univercity', models.CharField(blank=True, max_length=100, null=True)),
                ('other_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('other_year', models.CharField(blank=True, default=True, max_length=4, null=True)),
                ('skill', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('emails', models.EmailField(blank=True, max_length=100, null=True)),
                ('refference', models.CharField(blank=True, max_length=100, null=True)),
                ('relationships', models.CharField(blank=True, max_length=100, null=True)),
                ('belongs_department', models.CharField(blank=True, max_length=100, null=True)),
                ('joining_date', models.CharField(max_length=100)),
                ('living_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(default='absent', max_length=100)),
                ('date', models.CharField(blank=True, default='09-03-2021', max_length=100)),
                ('trainer_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TraineeAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(default='absent', max_length=100)),
                ('date', models.CharField(blank=True, default='09-03-2021', max_length=100)),
                ('trainee_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.trainee')),
            ],
        ),
        migrations.CreateModel(
            name='StaffAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, default='09-03-2021', max_length=100)),
                ('staff_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('tds', models.CharField(max_length=100)),
                ('basic', models.IntegerField()),
                ('pf', models.IntegerField()),
                ('da', models.IntegerField()),
                ('prof_tax', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('ta', models.IntegerField()),
                ('deductions', models.CharField(max_length=100)),
                ('medical_allowance', models.IntegerField()),
                ('other', models.IntegerField()),
                ('net_salary', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
            ],
        ),
        migrations.CreateModel(
            name='InternAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, default='09-03-2021', max_length=100)),
                ('intern_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.intern')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, default='09-03-2021', max_length=100)),
                ('emp_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
            ],
        ),
    ]
