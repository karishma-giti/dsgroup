from django.db import models
from datetime import date 

gender=(
    ('Male','Male'),
    ('Female','Female'),
)


# Create your models here.
class Intern(models.Model):  
<<<<<<< HEAD
    profile = models.FileField(upload_to='media/',blank=True,null=True,default=True)  
    intern_name = models.CharField(max_length=100,default=True)  
    email = models.EmailField(max_length=100,default=True) 
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.IntegerField(blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True,default=True)  
    date_of_birth = models.CharField(max_length=100,default=True) 
    blood_group = models.CharField(max_length=100,blank=True,null=True,default=True)  
    father_name = models.CharField(max_length=100,default=True)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True,default=True)  
    father_no = models.IntegerField(blank=True,null=True,default=True)   
    city = models.CharField(max_length=100,default=True)  
    state = models.CharField(max_length=100,default=True)  
    pin_code = models.IntegerField(blank=True,null=True,default=True)   
    address = models.CharField(max_length=100,default=True)  
    join_date = models.CharField(max_length=100,default=True)
    school_name = models.CharField(max_length=100,blank=True,null=True,default=True)
    board = models.CharField(max_length=100,blank=True,null=True,default=True)
    passing_year = models.IntegerField(blank=True,null=True,default=True) 
    school_marksheet = models.FileField(upload_to='media/',blank=True,null=True,default=True) 

    high_school_name = models.CharField(max_length=100,blank=True,null=True,default=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True,default=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True,default=True) 
    high_school_marksheet =models.FileField(upload_to='media/',blank=True,null=True,default=True) 

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    graduation_year =models.IntegerField(blank=True,null=True,default=True) 
    graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True,default=True) 
=======
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    intern_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.IntegerField(blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.CharField(max_length=100) 
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.IntegerField(blank=True,null=True) 

    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True) 

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.IntegerField(blank=True,null=True) 
>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc

    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_year = models.IntegerField(blank=True,null=True) 
<<<<<<< HEAD
    post_graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True,default=True) 
    
    other_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    other_year = models.IntegerField(blank=True,null=True,default=True) 
    other_marksheet = models.FileField(upload_to='media/',blank=True,null=True,default=True) 
=======
    
    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_year = models.IntegerField(blank=True,null=True)  
>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc
        
    def __str__(self): 
         return self.intern_name

<<<<<<< HEAD
class InternAttendance(models.Model):
    intern_name= models.ForeignKey('Intern',on_delete=models.CASCADE,default=True)
    attendance = models.CharField(max_length=100) 
    date=models.CharField(max_length=100,default=date.today().strftime("%d/%m/%Y"), blank=True) 

    def __str__(self): 
        return str(self.intern_name)

=======
>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc


class Trainer(models.Model):  
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    trainer_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 

    aadhar_no = models.IntegerField()   
    pan_card = models.IntegerField(blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.CharField(max_length=100) 
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)

    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.IntegerField(blank=True,null=True) 
    
    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True) 
    

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.IntegerField(blank=True,null=True) 

    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year = models.IntegerField(blank=True,null=True) 
    
    
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_year = models.IntegerField(blank=True,null=True) 
    

    skill = models.CharField(max_length=100,blank=True,null=True)
    position = models.CharField(max_length=100,blank=True,null=True)
    experience = models.CharField(max_length=100,blank=True,null=True)

    company_name = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=100,blank=True,null=True)
    contact_no = models.IntegerField(blank=True,null=True) 
    emails = models.EmailField(max_length=100,blank=True,null=True) 
    refference = models.CharField(max_length=100,blank=True,null=True)
    relationships = models.CharField(max_length=100,blank=True,null=True)
    belongs_department= models.CharField(max_length=100,blank=True,null=True)
    joining_date = models.CharField(max_length=100) 
    living_date =  models.CharField(max_length=100) 

    def __str__(self): 
         return "Trainer_name"


class Trainee(models.Model):
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    trainee_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.IntegerField(blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.CharField(max_length=100) 
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)

    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.IntegerField() 

    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True) 

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.IntegerField(blank=True,null=True) 

    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year = models.IntegerField(blank=True,null=True) 

    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_year = models.IntegerField(blank=True,null=True) 
<<<<<<< HEAD
    other_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
=======

>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc
 

    def __str__(self): 
         return "trainee_name"


<<<<<<< HEAD
class Trainee_attendence(models.Model):
    attendance = models.CharField(max_length=100) 
    date = models.CharField(max_length=100) 

    def __str__(self): 
         return "id"
 

class Employee(models.Model):  
    Profile = models.FileField(upload_to='media/',blank=True,null=True)  
    emp_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
=======


class Employee(models.Model):  
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    emp_name = models.CharField(max_length=100,default=True)  
    email = models.EmailField(max_length=100,default=True) 
>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.IntegerField(blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
<<<<<<< HEAD
    date_of_birth = models.CharField(max_length=100) 
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    percent = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.IntegerField(blank=True,null=True) 
    school_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True) 
    high_school_percent = models.CharField(max_length=100,blank=True,null=True)
    high_school_marksheet =models.FileField(upload_to='media/',blank=True,null=True) 
    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_percent = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.IntegerField(blank=True,null=True) 
    graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year = models.IntegerField(blank=True,null=True) 
    post_graduation_percent = models.CharField(max_length=100)
    post_graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_year = models.IntegerField(blank=True,null=True) 
    other_percent = models.CharField(max_length=100,blank=True,null=True)
    other_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
    skill = models.CharField(max_length=100,blank=True,null=True)
    position = models.CharField(max_length=100,blank=True,null=True)
    experience = models.CharField(max_length=100,blank=True,null=True)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=100,blank=True,null=True)
    contact_no = models.IntegerField(blank=True,null=True) 
    email = models.EmailField(max_length=100,blank=True,null=True) 
    gotdetail = models.CharField(max_length=100,blank=True,null=True)
    relationships = models.CharField(max_length=100,blank=True,null=True)
    belongs_department= models.CharField(max_length=100,blank=True,null=True)
=======
    date_of_birth = models.CharField(max_length=100,default=True) 
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100,default=True)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True,default=True)   
    city = models.CharField(max_length=100,default=True)  
    state = models.CharField(max_length=100,default=True)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100,default=True)  
    join_date = models.CharField(max_length=100,default=True)
    
    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.IntegerField(blank=True,null=True,default=True) 

    high_school_name = models.CharField(max_length=100,blank=True,null=True,default=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True,default=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True,default=True) 
    
 
    graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    graduation_year =models.IntegerField(blank=True,null=True,default=True) 
    
    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_year = models.IntegerField(blank=True,null=True,default=True) 

     
    other_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    other_year = models.IntegerField(blank=True,null=True,default=True) 

    skill = models.CharField(max_length=100,blank=True,null=True,default=True)
    position = models.CharField(max_length=100,blank=True,null=True,default=True)
    experience = models.CharField(max_length=100,blank=True,null=True,default=True)

    company_name = models.CharField(max_length=100,blank=True,null=True,default=True)
    designation = models.CharField(max_length=100,blank=True,null=True,default=True)
    contact_no = models.IntegerField(blank=True,null=True,default=True) 
    emails = models.EmailField(max_length=100,blank=True,null=True,default=True) 
    refference = models.CharField(max_length=100,blank=True,null=True,default=True)
    relationships = models.CharField(max_length=100,blank=True,null=True ,default=True)
    belongs_department= models.CharField(max_length=100,blank=True,null=True ,default=True)
    joining_date = models.CharField(max_length=100,default=True) 
    living_date =  models.CharField(max_length=100,default=True) 
>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc

    def __str__(self): 
         return str(self.emp_name)

<<<<<<< HEAD

class Employee_attendence(models.Model):
    attendance = models.CharField(max_length=100) 
    date = models.CharField(max_length=100) 

    def __str__(self): 
         return "id"
 
class Salary(models.Model):
    emp_name= models.ForeignKey('Employee',on_delete=models.CASCADE)
    salary = models.IntegerField() 
    tds =  models.IntegerField() 
    basic = models.IntegerField() 
    pf = models.IntegerField()   
    da =  models.IntegerField()   
    prof_tax =  models.IntegerField() 
    hra =  models.IntegerField()  
    deductions =  models.IntegerField()  
    medical_allowance =  models.IntegerField()  
    net_salary =  models.IntegerField()  
    sub_total =  models.IntegerField()  

    def __str__(self): 
         return str(self.emp_name)
       

=======
>>>>>>> 1502733a434305e2a2f08a65841962f0923d3ddc
 


class Staff(models.Model):  
    staff_id= models.CharField(max_length=20,unique=True,null=True)
    staff_name = models.CharField(max_length=100)  
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField(blank=True,null=True)   
    role = models.CharField(max_length=100)    
    join_date = models.CharField(max_length=100)
    
    def __str__(self): 
         return "staff_name"

