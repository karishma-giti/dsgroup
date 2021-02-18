from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    
    path('',views.dashboard, name='dashboard'),
    path('register_intern/',views.register_intern, name='register_intern'),
    path('view_interns/',views.view_interns, name='view_interns'),
    path('interns_attendence/',views.interns_attendence, name='interns_attendence'),
    path('intern_profile/<int:id>',views.intern_profile,name="intern_profile"),
    path('edit_intern/<int:id>',views.edit_intern,name='edit_intern'),
    path('manage_intern/<int:id>',views.manage_intern,name='manage_intern'),
    path('remove_intern/<int:id>',views.remove_intern,name='remove_intern'),


    path('register_trainees/',views.register_trainees, name='register_trainees'),
    path('view_trainees/',views.view_trainees, name='view_trainees'),
    path('trainees_attendence/',views.trainees_attendence, name='trainees_attendence'),

    path('register_employees/',views.register_employees, name='register_employees'),
    path('view_employees/',views.view_employees, name='view_employees'),
    path('employees_attendence/',views.employees_attendence, name='employees_attendence'),

    path('add_salary/',views.add_salary, name='add_salary'),
    path('view_salary/',views.view_salary, name='view_salary'),


    path('register_staff/',views.register_staff, name='register_staff'),
    path('view_staff/',views.view_staff, name='view_staff'),
    path('delete_staff/<int:id>',views.delete_staff,name='delete_staff'),
    path('edit_staff/<int:id>',views.edit_staff,name="edit_staff"),
    path('manage_staff/<int:id>', views.manage_staff,name="manage_staff"),
    path('staff_attendence',views.staff_attendence, name='staff_attendence'),
]
