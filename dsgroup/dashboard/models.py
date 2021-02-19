from django.db import models


gender=(
    ('Male','Male'),
    ('Female','Female'),
)


# Create your models here.
class Intern(models.Model):  
    intern_id= models.CharField(max_length=20,unique=True)
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
    school_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 

    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True) 
    high_school_marksheet =models.FileField(upload_to='media/',blank=True,null=True) 

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.IntegerField(blank=True,null=True) 
    graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 

    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year = models.IntegerField(blank=True,null=True) 
    post_graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
    
    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_year = models.IntegerField(blank=True,null=True) 
    other_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
        
    def __str__(self): 
         return "intern_name"



class Trainer(models.Model):  
    Trainer_id= models.CharField(max_length=20,unique=True,null=True)
    Profile = models.FileField(upload_to='media/',blank=True,null=True)  
    Trainer_name = models.CharField(max_length=100)  
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

    def __str__(self): 
         return "Trainer_name"




class Trainee(models.Model):
    trainee_id= models.CharField(max_length=20,unique=True)
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
    school_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 

    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.IntegerField(blank=True,null=True) 
    high_school_marksheet =models.FileField(upload_to='media/',blank=True,null=True) 

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_percent = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.IntegerField(blank=True,null=True) 
    graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 

    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year = models.IntegerField(blank=True,null=True) 
    post_graduation_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 

    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_year = models.IntegerField(blank=True,null=True) 
    other_marksheet = models.FileField(upload_to='media/',blank=True,null=True) 
 

    def __str__(self): 
         return "trainee_name"


class Employee(models.Model):  
    emp_id= models.CharField(max_length=20,unique=True,null=True)
    Profile = models.FileField(upload_to='media/',blank=True,null=True)  
    emp_name = models.CharField(max_length=100)  
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

    def __str__(self): 
         return "emp_name"


class Staff(models.Model):  
    staff_id= models.CharField(max_length=20,unique=True,null=True)
    staff_name = models.CharField(max_length=100)  
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField(blank=True,null=True)   
    role = models.CharField(max_length=100)    
    join_date = models.CharField(max_length=100)
    
    def __str__(self): 
         return "staff_name"
