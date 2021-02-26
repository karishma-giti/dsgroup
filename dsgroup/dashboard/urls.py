from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    
    path('',views.dashboard, name='dashboard'),
    path('register_intern/',views.register_intern, name='register_intern'),
    path('view_interns/',views.view_interns, name='view_interns'),
    path('interns_attendance/',views.interns_attendance, name='interns_attendance'),
    path('interns_attendance_date/',views.interns_attendance_date, name='interns_attendance_date'),
    path('interns_attendance_edit/<int:id>',views.interns_attendance_edit, name='interns_attendance_edit'),
    path('interns_attendance_manage/<int:id>',views.interns_attendance_manage, name='interns_attendance_manage'),
    path('intern_profile/<int:id>',views.intern_profile,name="intern_profile"),
    path('edit_intern/<int:id>',views.edit_intern,name='edit_intern'),
    path('manage_intern/<int:id>',views.manage_intern,name='manage_intern'),
    path('remove_intern/',views.remove_intern,name='remove_intern'),


    path('register_trainees/',views.register_trainees, name='register_trainees'),
    path('view_trainees/',views.view_trainees, name='view_trainees'),
    path('trainee_attendance/',views.trainee_attendance, name='trainee_attendance'),
    path('trainee_attendance_date/',views.trainee_attendance_date, name='trainee_attendance_date'),
    path('trainee_attendance_edit/<int:id>',views.trainee_attendance_edit, name='trainee_attendance_edit'),
    path('trainee_attendance_manage/<int:id>',views.trainee_attendance_manage, name='trainee_attendance_manage'),
    # path('trainees_profile/<int:id>',views.trainees_profile,name="trainees_profile"),
    path('edit_trainees/<int:id>',views.edit_trainees,name='edit_trainees'),
    path('manage_trainees/<int:id>',views.manage_trainees,name='manage_trainees'),
    path('remove_trainees/',views.remove_trainees,name='remove_trainees'),

    path('register_trainer',views.register_trainer,name='register_trainer'),
    path('view_trainer',views.view_trainer,name='view_trainer'),
    path('trainer_attendance/',views.trainer_attendance, name='trainer_attendance'),
    path('trainer_attendance_date/',views.trainer_attendance_date, name='trainer_attendance_date'),
    path('trainer_attendance_edit/<int:id>',views.trainer_attendance_edit, name='trainer_attendance_edit'),
    path('trainer_attendance_manage/<int:id>',views.trainer_attendance_manage, name='trainer_attendance_manage'),
    path('edit_trainer/<int:id>',views.edit_trainer,name='edit_trainer'),
    path('manage_trainer/<int:id>',views.manage_trainer,name='manage_trainer'),
    path('remove_trainer',views.remove_trainer,name='remove_trainer'),

    path('register_employees/',views.register_employees, name='register_employees'),
    path('view_employees/',views.view_employees, name='view_employees'),
    path('emp_attendance/',views.emp_attendance, name='emp_attendance'),
    path('emp_attendance_date/',views.emp_attendance_date, name='emp_attendance_date'),
    path('emp_attendance_edit/<int:id>',views.emp_attendance_edit, name='emp_attendance_edit'),
    path('emp_attendance_manage/<int:id>',views.emp_attendance_manage, name='emp_attendance_manage'),
    path('edit_employees/<int:id>',views.edit_employees,name='edit_employees'),
    path('manage_employees/<int:id>',views.manage_employees,name='manage_employees'),
    path('remove_employees/',views.remove_employees,name='remove_employees'),

    path('add_salary/',views.add_salary, name='add_salary'),
    path('salary_detail/<int:id>',views.salary_detail, name='salary_detail'),
    path('view_salary/',views.view_salary, name='view_salary'),


    path('register_staff/',views.register_staff, name='register_staff'),
    path('view_staff/',views.view_staff, name='view_staff'),
    path('search/',views.search, name='search'),
    path('staff_attendance/',views.staff_attendance, name='staff_attendance'),
    path('staff_attendance_date/',views.staff_attendance_date, name='staff_attendance_date'),
    path('staff_attendance_edit/<int:id>',views.staff_attendance_edit, name='staff_attendance_edit'),
    path('staff_attendance_manage/<int:id>',views.staff_attendance_manage, name='staff_attendance_manage'),
    path('delete_staff/<int:id>',views.delete_staff,name='delete_staff'),
    path('edit_staff/<int:id>',views.edit_staff,name="edit_staff"),
    path('manage_staff/<int:id>', views.manage_staff,name="manage_staff"),
   
]
