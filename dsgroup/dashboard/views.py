from django.shortcuts import render, redirect  
from django.http import HttpResponse,HttpResponseRedirect
from .models import Intern,Staff,Trainee,Salary,Employee,InternAttendance
from datetime import date




############################################################## Intern ########################################################  


def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def register_intern(request):
    interns = Intern(request.POST,request.FILES)
    if request.method =="POST":
        profile=request.FILES.get('profile')
        intern_name=request.POST.get('intern_name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        aadhar_no=request.POST.get('aadhar_no')
        pan_card=request.POST.get('pan_card')
        gender=request.POST.get('gender')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_no=request.POST.get('father_no')
        city=request.POST.get('city')
        state = request.POST.get('state')
        pin_code=request.POST.get('pin_code')
        address=request.POST.get('address')
        join_date=request.POST.get('join_date')

        school_name=request.POST.get('school_name')
        board=request.POST.get('board')
        passing_year=request.POST.get('passing_year')

        high_school_name=request.POST.get('high_school_name')
        high_school_board=request.POST.get('high_school_board')
        high_school_passing_year=request.POST.get('high_school_passing_year')

        graduation_univercity=request.POST.get('graduation_univercity')
        graduation_degree=request.POST.get('graduation_degree')
        graduation_year=request.POST.get('graduation_year')
        
        post_graduation_univercity=request.POST.get('post_graduation_univercity')
        post_graduation_degree=request.POST.get('post_graduation_degree')
        post_graduation_year=request.POST.get('post_graduation_year')
    
        other_univercity =request.POST.get('other_univercity')
        other_degree=request.POST.get('other_degree')
        other_year=request.POST.get('other_year')

        Insertion=Intern(profile=profile, intern_name= intern_name,email=email, phone_no= phone_no, aadhar_no= aadhar_no,
        pan_card=pan_card,gender=gender,date_of_birth=date_of_birth,blood_group=blood_group,father_name=father_name,
        father_occupation=father_occupation,father_no=father_no,city=city,pin_code=pin_code,address=address,join_date=join_date
        ,school_name=school_name,board=board, passing_year=passing_year,high_school_name=high_school_name
        ,high_school_board=high_school_board,high_school_passing_year=high_school_passing_year,
        graduation_univercity=graduation_univercity,graduation_degree=graduation_degree, graduation_year= graduation_year,
        post_graduation_degree=post_graduation_degree,post_graduation_univercity=post_graduation_univercity
        ,post_graduation_year=post_graduation_year,
        other_degree=other_degree,other_univercity=other_univercity,other_year=other_year,state=state)
        Insertion.save()
        return render(request,"dashboard/register_intern.html")
    else:
        return render(request,"dashboard/register_intern.html")

################ view intern ##################      

def view_interns(request):
    data = Intern(request.GET)
    interns = Intern.objects.all()
    print(interns)
    return render(request,"dashboard/view_intern.html",{'view_intern':interns} )
    
    
################ intern profile##################  
def intern_profile(request,id):
    interns = Intern.objects.filter(id=id)
    print(interns)
    return render(request,"dashboard/intern_profile.html")
    

def interns_attendance(request): 
    if request.method =="POST":
        print(request.POST)
        intern_name=Intern.objects.get(intern_name=request.POST['internname'])
        attendance = request.POST.get('attendance')
        Insertion=InternAttendance(intern_name=intern_name,attendance=attendance)
        Insertion.save()
        return render(request,"dashboard/interns_attendance.html")
    else:
        data = Intern.objects.all()
        dat = date.today().strftime("%d/%m/%Y")
        print(data)
        return render(request,"dashboard/interns_attendance.html",{'data':data,'dat':dat})


def interns_attendance_date(request):
    data = InternAttendance.objects.all()
    
    return render(request,"dashboard/interns_attendance_date.html",{'data':data})
 

def interns_attendance_edit(request,id):
    data = InternAttendance.objects.get(id=id)
    print(data)
    return render(request,"dashboard/interns_attendance_edit.html",{'data':data})

def interns_attendance_manage(request,id):
    print(id)
    data = InternAttendance.objects.get(id=id)
    if request.method == "POST":
        print(request.POST.get('attendance') )

        data.attendance = request.POST.get('attendance') 
        data.save()
    return redirect(f'/dashboard/interns_attendance_edit/{id}',{'data':data})

  
################ edit intern ##################  
def edit_intern(request,id):
    interns = Intern.objects.get(id=id)
    print(interns)
    return render(request,"dashboard/edit_intern.html",{'edit_intern':interns}) 


################ update intern ##################  
def manage_intern(request,id):
    interns = Intern.objects.get(id=id) 
    if request.method =="POST":
        if "profile" in request.FILES:
            img=request.FILES["profile"]
            interns.profile =img
        interns.save()
        interns.intern_name=request.POST.get('intern_name','')
        interns.email=request.POST.get('email','')
        interns.phone_no=request.POST.get('phone_no','')
        interns.aadhar_no=request.POST.get('aadhar_no','')
        interns.pan_card=request.POST.get('pan_card','')
        interns.gender=request.POST.get('gender','')
        interns.date_of_birth=request.POST.get('date_of_birth','')
        interns.blood_group=request.POST.get('blood_group','')
        interns.father_name=request.POST.get('father_name','')
        interns.father_occupation=request.POST.get('father_occupation','')
        interns.father_no=request.POST.get('father_no','')
        interns.city=request.POST.get('city','')
        interns.state = request.POST.get('state','')
        interns.pin_code=request.POST.get('pin_code','')
        interns.address=request.POST.get('address','')
        interns.join_date=request.POST.get('join_date','')

        interns.school_name=request.POST.get('school_name','')
        interns.board=request.POST.get('board','')
        interns.passing_year=request.POST.get('passing_year','')
        
        interns.high_school_name=request.POST.get('high_school_name','')
        interns.high_school_board=request.POST.get('high_school_board','')
        interns.high_school_passing_year=request.POST.get('high_school_passing_year','')
        
        interns.graduation_univercity=request.POST.get('graduation_univercity','')
        interns.graduation_degree=request.POST.get('graduation_degree','')
        interns.graduation_year=request.POST.get('graduation_year','')
        
        
        interns.post_graduation_univercity=request.POST.get('post_graduation_univercity','')
        interns.post_graduation_degree=request.POST.get('post_graduation_degree','')
        interns.post_graduation_year=request.POST.get('post_graduation_year','')
       
       
        interns.other_univercity =request.POST.get('other_univercity','')
        interns.other_degree=request.POST.get('other_degree','')
        interns.other_year=request.POST.get('other_year','')
        interns.save()
    return redirect('/dashboard/view_interns')

################ delete intern ##################  
def remove_intern(request):
    Id=request.POST['inter_id']
    print(Id)
    interns = Intern.objects.get(pk=Id)
    interns.delete()
    return redirect('/dashboard/view_interns')       

############################################################## employee departmenet ########################################################  


def register_trainees(request):
    trainee = Trainee(request.POST,request.FILES)
    if request.method =="POST":
        profile=request.FILES.get('profile')
        trainee_name=request.POST.get('trainee_name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        aadhar_no=request.POST.get('aadhar_no')
        pan_card=request.POST.get('pan_card')
        gender=request.POST.get('gender')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_no=request.POST.get('father_no')
        city=request.POST.get('city')
        state = request.POST.get('state')
        pin_code=request.POST.get('pin_code')
        address=request.POST.get('address')
        join_date=request.POST.get('join_date')

        school_name=request.POST.get('school_name')
        board=request.POST.get('board')
        passing_year=request.POST.get('passing_year')

        high_school_name=request.POST.get('high_school_name')
        high_school_board=request.POST.get('high_school_board')
        high_school_passing_year=request.POST.get('high_school_passing_year')

        graduation_univercity=request.POST.get('graduation_univercity')
        graduation_degree=request.POST.get('graduation_degree')
        graduation_year=request.POST.get('graduation_year')
        
        post_graduation_univercity=request.POST.get('post_graduation_univercity')
        post_graduation_degree=request.POST.get('post_graduation_degree')
        post_graduation_year=request.POST.get('post_graduation_year')
       
        other_univercity =request.POST.get('other_univercity')
        other_degree=request.POST.get('other_degree')
        other_year=request.POST.get('other_year')

        Insertion=Trainee(profile=profile, trainee_name= trainee_name,email=email, phone_no= phone_no, aadhar_no= aadhar_no,
        pan_card=pan_card,gender=gender,date_of_birth=date_of_birth,blood_group=blood_group,father_name=father_name,
        father_occupation=father_occupation,father_no=father_no,city=city,pin_code=pin_code,address=address,join_date=join_date
        ,school_name=school_name,board=board, passing_year=passing_year,high_school_name=high_school_name
        ,high_school_board=high_school_board,high_school_passing_year=high_school_passing_year,
        graduation_univercity=graduation_univercity,graduation_degree=graduation_degree, graduation_year= graduation_year,
        post_graduation_degree=post_graduation_degree,post_graduation_univercity=post_graduation_univercity
        ,post_graduation_year=post_graduation_year,
        other_degree=other_degree,other_univercity=other_univercity,other_year=other_year,state=state)
        Insertion.save()
        return render(request,"dashboard/register_trainees.html")
    else:
        return render(request,"dashboard/register_trainees.html")

################ view trainees ##################          

def view_trainees(request):
    data = Trainee(request.GET)
    trainees = Trainee.objects.all()
    print(trainees)
    return render(request,"dashboard/view_trainees.html",{'view_trainees':trainees} )


# def trainees_profile(request,id):
#     interns = Intern.objects.filter(id=id)
#     print(interns)
#     return render(request,"dashboard/intern_profile.html")
        

################ edit trainees ##################  
def edit_trainees(request,id):
    trainees = Trainee.objects.get(id=id)
    print(trainees)
    return render(request,"dashboard/edit_trainees.html",{'edit_trainees':trainees})  


################ update trainees ##################  
def manage_trainees(request,id):
    trainees = Trainee.objects.get(id=id) 
    if request.method =="POST":
        if "profile" in request.FILES:
            img=request.FILES["profile"]
            interns.profile =img
        trainees.save()
        trainees.trainee_name=request.POST.get('trainee_name','')
        trainees.email=request.POST.get('email','')
        trainees.phone_no=request.POST.get('phone_no','')
        trainees.aadhar_no=request.POST.get('aadhar_no','')
        trainees.pan_card=request.POST.get('pan_card','')
        trainees.gender=request.POST.get('gender','')
        trainees.date_of_birth=request.POST.get('date_of_birth','')
        trainees.blood_group=request.POST.get('blood_group','')
        trainees.father_name=request.POST.get('father_name','')
        trainees.father_occupation=request.POST.get('father_occupation','')
        trainees.father_no=request.POST.get('father_no','')
        trainees.city=request.POST.get('city','')
        trainees.state = request.POST.get('state','')
        trainees.pin_code=request.POST.get('pin_code','')
        trainees.address=request.POST.get('address','')
        trainees.join_date=request.POST.get('join_date','')

        trainees.school_name=request.POST.get('school_name','')
        trainees.board=request.POST.get('board','')
        trainees.passing_year=request.POST.get('passing_year','')

        trainees.high_school_name=request.POST.get('high_school_name','')
        trainees.high_school_board=request.POST.get('high_school_board','')
        trainees.high_school_passing_year=request.POST.get('high_school_passing_year','')
    
        trainees.graduation_univercity=request.POST.get('graduation_univercity','')
        trainees.graduation_degree=request.POST.get('graduation_degree','')
        trainees.graduation_year=request.POST.get('graduation_year','')
        
        trainees.post_graduation_univercity=request.POST.get('post_graduation_univercity','')
        trainees.post_graduation_degree=request.POST.get('post_graduation_degree','')
        trainees.post_graduation_year=request.POST.get('post_graduation_year','')

       
        trainees.other_univercity =request.POST.get('other_univercity','')
        trainees.other_degree=request.POST.get('other_degree','')
        trainees.other_year=request.POST.get('other_year','')
        trainees.save()
    return redirect('/dashboard/view_trainees')


################ delete trainees ##################  
def remove_trainees(request):
    Id=request.POST['trainee_id']
    print(Id)
    trainees = Trainee.objects.get(pk=Id)
    trainees.delete()
    return redirect('/dashboard/view_trainees')       


################ trainees attendence ##################  
def trainees_attendence(request):
    return render(request,"dashboard/trainees_attendence.html")

############################################################################################################################################    

def register_employees(request):
    return render(request,"dashboard/register_employees.html")
############################################################## employee departmenet ########################################################  

def register_employees(request):
    employee = Employee(request.POST,request.FILES)
    if request.method =="POST":
        profile=request.FILES.get('profile')
        emp_name=request.POST.get('emp_name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        aadhar_no=request.POST.get('aadhar_no')
        pan_card=request.POST.get('pan_card')
        gender=request.POST.get('gender')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_no=request.POST.get('father_no')
        city=request.POST.get('city')
        state = request.POST.get('state')
        pin_code=request.POST.get('pin_code')
        address=request.POST.get('address')
        join_date=request.POST.get('join_date')

        school_name=request.POST.get('school_name')
        board=request.POST.get('board')
        passing_year=request.POST.get('passing_year')

        high_school_name=request.POST.get('high_school_name')
        high_school_board=request.POST.get('high_school_board')
        high_school_passing_year=request.POST.get('high_school_passing_year')

        graduation_univercity=request.POST.get('graduation_univercity')
        graduation_degree=request.POST.get('graduation_degree')
        graduation_year=request.POST.get('graduation_year')

        
        post_graduation_univercity=request.POST.get('post_graduation_univercity')
        post_graduation_degree=request.POST.get('post_graduation_degree')
        post_graduation_year=request.POST.get('post_graduation_year')

       
        other_univercity =request.POST.get('other_univercity')
        other_degree=request.POST.get('other_degree')
        other_year=request.POST.get('other_year')


        skill = request.POST.getlist(('skill[]'))
        skill=','.join(skill)
        print(skill)
        position = request.POST.getlist(str('position[]'))
        position=','.join(position)

        print(position)
        experience = request.POST.getlist(str('experience[]'))
        experience=','.join(experience)
        print(experience)

        company_name = request.POST.get('company_name')
        designation =request.POST.get('designation')
        contact_no = request.POST.get('contact_no')
        emails = request.POST.get('emails')
        refference = request.POST.get('refference')
        relationships = request.POST.get('relationships')
        belongs_department= request.POST.get('belongs_department')
        joining_date = request.POST.get('joining_date')
        living_date = request.POST.get('living_date')

        Insertion=Employee(profile=profile, emp_name= emp_name,email=email, phone_no= phone_no, aadhar_no= aadhar_no,
        pan_card=pan_card,gender=gender,date_of_birth=date_of_birth,blood_group=blood_group,father_name=father_name,
        father_occupation=father_occupation,father_no=father_no,city=city,pin_code=pin_code,address=address,join_date=join_date,
        school_name=school_name,board=board,passing_year=passing_year,high_school_name=high_school_name,
        high_school_board=high_school_board,high_school_passing_year=high_school_passing_year,
        graduation_univercity=graduation_univercity,graduation_degree=graduation_degree, graduation_year= graduation_year,
        post_graduation_degree=post_graduation_degree,post_graduation_univercity=post_graduation_univercity,
        post_graduation_year=post_graduation_year,
        other_degree=other_degree,other_univercity=other_univercity,other_year=other_year,state=state,skill=skill,position=position,
        experience=experience,company_name=company_name,designation=designation,contact_no=contact_no,emails=emails,refference=refference,
        relationships=relationships,belongs_department=belongs_department,joining_date=joining_date,living_date=living_date)
        Insertion.save()
        print(Insertion)
        return render(request,"dashboard/register_employees.html")
    else:
        return render(request,"dashboard/register_employees.html")


################ view employees ##################  
def view_employees(request):
    data = Employee(request.GET)
    employees = Employee.objects.all()
    print(employees)
    return render(request,"dashboard/view_employees.html",{'view_employees':employees} )


################ employees attendence ################## 
def employees_attendence(request):
    return render(request,"dashboard/employees_attendence.html")


############################################################################################################################################ 
################ edit employees ################## 
def edit_employees(request,id):
    employees = Employee.objects.get(id=id)
    skills=list(employees.skill.split(","))
    positions=list(employees.position.split(","))
    experiences=list(employees.experience.split(","))
    print(employees)
    skill_info=zip(skills,positions,experiences)
    print(type(skill_info))
    return render(request,"dashboard/edit_employees.html",{'edit_employees':employees,'skills':skill_info})

################ manage employees ################## 
def manage_employees(request,id):
    employee = Employee.objects.get(id=id) 
    if request.method =="POST":
        employee.profile=request.FILES.get('profile','')
        employee.emp_name=request.POST.get('emp_name','')
        employee.email=request.POST.get('email','')
        employee.phone_no=request.POST.get('phone_no','')
        employee.aadhar_no=request.POST.get('aadhar_no','')
        employee.pan_card=request.POST.get('pan_card','')
        employee.gender=request.POST.get('gender','')
        employee.date_of_birth=request.POST.get('date_of_birth','')
        employee.blood_group=request.POST.get('blood_group','')
        employee.father_name=request.POST.get('father_name','')
        employee.father_occupation=request.POST.get('father_occupation','')
        employee.father_no=request.POST.get('father_no','')
        employee.city=request.POST.get('city','')
        employee.state = request.POST.get('state','')
        employee.pin_code=request.POST.get('pin_code','')
        employee.address=request.POST.get('address','')
        employee.join_date=request.POST.get('join_date','')

        employee.school_name=request.POST.get('school_name','')
        employee.board=request.POST.get('board','')
        employee.passing_year=request.POST.get('passing_year','')


        employee.high_school_name=request.POST.get('high_school_name','')
        employee.high_school_board=request.POST.get('high_school_board','')
        employee.high_school_passing_year=request.POST.get('high_school_passing_year','')

        employee.graduation_univercity=request.POST.get('graduation_univercity','')
        employee.graduation_degree=request.POST.get('graduation_degree','')
        employee.graduation_year=request.POST.get('graduation_year','')

        
        employee.post_graduation_univercity=request.POST.get('post_graduation_univercity','')
        employee.post_graduation_degree=request.POST.get('post_graduation_degree','')
        employee.post_graduation_year=request.POST.get('post_graduation_year','')
        

        employee.other_univercity =request.POST.get('other_univercity','')
        employee.other_degree=request.POST.get('other_degree','')
        employee.other_year=request.POST.get('other_year','')


        employee.skill = request.POST.getlist(('skill[]'))
        employee.skill=','.join(employee.skill)
        print(employee.skill)
        employee.position = request.POST.getlist(str('position[]'))
        employee.position=','.join( employee.position)

        print( employee.position)
        employee.experience = request.POST.getlist(str('experience[]'))
        employee.experience=','.join(employee.experience)
        print(employee.experience)

        employee.company_name = request.POST.get('company_name','')
        employee.designation =request.POST.get('designation','')
        employee.contact_no = request.POST.get('contact_no','')
        employee.emails = request.POST.get('emails','')
        employee.refference = request.POST.get('refference','')
        employee.relationships = request.POST.get('relationships','')
        employee.belongs_department= request.POST.get('belongs_department','')
        employee.joining_date = request.POST.get('joining_date','')
        employee.living_date = request.POST.get('living_date','')
        employee.save()
    return redirect('/dashboard/view_employees')

################ delete employees ################## 
def remove_employees(request):
    Id=request.POST['employee_id']
    print(Id)
    employees = Employee.objects.get(pk=Id)
    employees.delete()
    return redirect('/dashboard/view_employees')       




############################################################## employee departmenet ########################################################  

def register_trainer(request):
    trainer = Trainer(request.POST,request.FILES)
    if request.method =="POST":
        profile=request.FILES.get('profile')
        trainer_name=request.POST.get('trainer_name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        aadhar_no=request.POST.get('aadhar_no')
        pan_card=request.POST.get('pan_card')
        gender=request.POST.get('gender')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_no=request.POST.get('father_no')
        city=request.POST.get('city')
        state = request.POST.get('state')
        pin_code=request.POST.get('pin_code')
        address=request.POST.get('address')
        join_date=request.POST.get('join_date')

        school_name=request.POST.get('school_name')
        board=request.POST.get('board')
        passing_year=request.POST.get('passing_year')

        high_school_name=request.POST.get('high_school_name')
        high_school_board=request.POST.get('high_school_board')
        high_school_passing_year=request.POST.get('high_school_passing_year')

        graduation_univercity=request.POST.get('graduation_univercity')
        graduation_degree=request.POST.get('graduation_degree')
        graduation_year=request.POST.get('graduation_year')
        
        post_graduation_univercity=request.POST.get('post_graduation_univercity')
        post_graduation_degree=request.POST.get('post_graduation_degree')
        post_graduation_year=request.POST.get('post_graduation_year')
       
        other_univercity =request.POST.get('other_univercity')
        other_degree=request.POST.get('other_degree')
        other_year=request.POST.get('other_year')


        skill = request.POST.getlist(('skill[]'))
        skill=','.join(skill)
        print(skill)
        position = request.POST.getlist(str('position[]'))
        position=','.join(position)

        print(position)
        experience = request.POST.getlist(str('experience[]'))
        experience=','.join(experience)
        print(experience)

        company_name = request.POST.get('company_name')
        designation =request.POST.get('designation')
        contact_no = request.POST.get('contact_no')
        emails = request.POST.get('emails')
        refference = request.POST.get('refference')
        relationships = request.POST.get('relationships')
        belongs_department= request.POST.get('belongs_department')
        joining_date = request.POST.get('joining_date')
        living_date = request.POST.get('living_date')

        Insertion=Trainer(profile=profile, trainer_name= trainer_name,email=email, phone_no= phone_no, aadhar_no= aadhar_no,
        pan_card=pan_card,gender=gender,date_of_birth=date_of_birth,blood_group=blood_group,father_name=father_name,
        father_occupation=father_occupation,father_no=father_no,city=city,pin_code=pin_code,address=address,join_date=join_date,
        school_name=school_name,board=board,passing_year=passing_year,high_school_name=high_school_name,
        high_school_board=high_school_board,high_school_passing_year=high_school_passing_year,
        graduation_univercity=graduation_univercity,graduation_degree=graduation_degree, graduation_year= graduation_year,
        post_graduation_degree=post_graduation_degree,post_graduation_univercity=post_graduation_univercity,
        post_graduation_year=post_graduation_year,other_degree=other_degree,other_univercity=other_univercity,other_year=other_year,state=state,skill=skill,position=position,
        experience=experience,company_name=company_name,designation=designation,contact_no=contact_no,emails=emails,refference=refference,
        relationships=relationships,belongs_department=belongs_department,joining_date=joining_date,living_date=living_date)
        Insertion.save()
        print(Insertion)
        return render(request,"dashboard/register_trainer.html")
    else:
        return render(request,"dashboard/register_trainer.html")


################ view trainer ################## 
def view_trainer(request):
    data = Trainer(request.GET)
    trainer = Trainer.objects.all()
    print(trainer)
    return render(request,"dashboard/view_trainer.html",{'view_trainers':trainer})


################ edit trainer ################## 
def edit_trainer(request,id):
    trainers = Trainer.objects.get(id=id)
    skills=list(trainers.skill.split(","))
    positions=list(trainers.position.split(","))
    experiences=list(trainers.experience.split(","))
    print(trainers)
    skill_info=zip(skills,positions,experiences)
    print(type(skill_info))
    return render(request,"dashboard/edit_trainer.html",{'edit_trainer':trainers,'skills':skill_info})

################ update trainer ################## 
def manage_trainer(request,id):
    trainer = Trainer.objects.get(id=id) 
    if request.method =="POST":
        trainer.profile=request.FILES.get('profile','')
        trainer.trainer_name=request.POST.get('trainer_name','')
        trainer.email=request.POST.get('email','')
        trainer.phone_no=request.POST.get('phone_no','')
        trainer.aadhar_no=request.POST.get('aadhar_no','')
        trainer.pan_card=request.POST.get('pan_card','')
        trainer.gender=request.POST.get('gender','')
        trainer.date_of_birth=request.POST.get('date_of_birth','')
        trainer.blood_group=request.POST.get('blood_group','')
        trainer.father_name=request.POST.get('father_name','')
        trainer.father_occupation=request.POST.get('father_occupation','')
        trainer.father_no=request.POST.get('father_no','')
        trainer.city=request.POST.get('city','')
        trainer.state = request.POST.get('state','')
        trainer.pin_code=request.POST.get('pin_code','')
        trainer.address=request.POST.get('address','')
        trainer.join_date=request.POST.get('join_date','')

        trainer.school_name=request.POST.get('school_name','')
        trainer.board=request.POST.get('board','')
        trainer.passing_year=request.POST.get('passing_year','')


        trainer.high_school_name=request.POST.get('high_school_name','')
        trainer.high_school_board=request.POST.get('high_school_board','')
        trainer.high_school_passing_year=request.POST.get('high_school_passing_year','')

        trainer.graduation_univercity=request.POST.get('graduation_univercity','')
        trainer.graduation_degree=request.POST.get('graduation_degree','')
        trainer.graduation_year=request.POST.get('graduation_year','')

        
        trainer.post_graduation_univercity=request.POST.get('post_graduation_univercity','')
        trainer.post_graduation_degree=request.POST.get('post_graduation_degree','')
        trainer.post_graduation_year=request.POST.get('post_graduation_year','')
        

        trainer.other_univercity =request.POST.get('other_univercity','')
        trainer.other_degree=request.POST.get('other_degree','')
        trainer.other_year=request.POST.get('other_year','')


        trainer.skill = request.POST.getlist(('skill[]'))
        trainer.skill=','.join(trainer.skill)
        print(trainer.skill)
        trainer.position = request.POST.getlist(str('position[]'))
        trainer.position=','.join( trainer.position)

        print( trainer.position)
        trainer.experience = request.POST.getlist(str('experience[]'))
        trainer.experience=','.join(trainer.experience)
        print(trainer.experience)

        trainer.company_name = request.POST.get('company_name','')
        trainer.designation =request.POST.get('designation','')
        trainer.contact_no = request.POST.get('contact_no','')
        trainer.emails = request.POST.get('emails','')
        trainer.refference = request.POST.get('refference','')
        trainer.relationships = request.POST.get('relationships','')
        trainer.belongs_department= request.POST.get('belongs_department','')
        trainer.joining_date = request.POST.get('joining_date','')
        trainer.living_date = request.POST.get('living_date','')
        trainer.save()
    return redirect('/dashboard/view_trainer')

    

################ delete trainer ################## 
def remove_trainer(request):
    Id=request.POST['trainer_id']
    print(Id)
    trainers = Trainer.objects.get(pk=Id)
    trainers.delete()
    return redirect('/dashboard/view_trainer')       




    

############################################################## employee departmenet ########################################################  


def add_salary(request):
    if request.method =="POST":
        print(request.POST)
        emp_name=Employee.objects.get(emp_name=request.POST['empname'])
        salary = request.POST['salary']
        tds = request.POST['tds']
        basic = request.POST['basic']
        pf =request.POST['pf']   
        da =  request.POST['da']   
        prof_tax = request.POST['prof_tax'] 
        hra = request.POST['hra'] 
        deductions = request.POST['deductions']
        medical_allowance = request.POST['medical_allowance']  
        net_salary = request.POST['net_salary']  
        sub_total = request.POST['sub_total']  

        Insertion=Salary(emp_name=emp_name,salary=salary,tds=tds,basic=basic,hra=hra,pf=pf,da=da,prof_tax=prof_tax,deductions=deductions,medical_allowance=medical_allowance
        ,net_salary=net_salary,sub_total=sub_total)
        Insertion.save()
        return render(request,"dashboard/view_salary.html")
    else:
        employee = Employee.objects.all()
        return render(request,"dashboard/add_salary.html",{'employee':employee})



    return render(request,"dashboard/view_salary.html")

def view_salary(request):
    data = Salary.objects.all()
    print(data)
    return render(request,"dashboard/view_salary.html",{'data':data})

def salary_detail(request,id):
    data = Salary.objects.get(id=id)
    return render(request,"dashboard/salary_detail.html",{'data':data})


############################################################## employee departmenet ########################################################  


def register_staff(request):
    if request.method =="POST":
        print(request.POST)
        staff_name=request.POST['staff_name']
        phone_no=request.POST['phone_no']
        aadhar_no=request.POST['aadhar_no']
        role=request.POST['role']
        join_date=request.POST['join_date']

        Insertion=Staff(staff_name=staff_name, phone_no= phone_no,aadhar_no=aadhar_no,role=role,join_date=join_date)
        Insertion.save()
        return render(request,"dashboard/register_staff.html")
    else:
        return render(request,"dashboard/register_staff.html")


    
################ view staff ##################        
def view_staff(request):
    data = Staff.objects.all()
    return render(request,"dashboard/view_staff.html",{'data':data})



################ delete staff ################## 
def delete_staff(request, id):
    staff=Staff.objects.filter(pk=id)
    staff.delete()
    return HttpResponseRedirect("/dashboard/view_staff")



################ edit staff ################## 
def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    print(staff)
    return render(request,"dashboard/edit_staff.html",{'staff':staff})



################ update staff ################## 
def manage_staff(request,id):
    staff = Staff.objects.get(id=id)
    if request.method == "POST":
        staff.staff_name = request.POST.get('staff_name','') 
        staff.phone_no = request.POST.get('phone_no','')
        staff.aadhar_no = request.POST.get('aadhar_no','')
        staff.role = request.POST.get('role','')
        staff.join_date = request.POST.get('join_date','')
        staff.save()
    return redirect('/dashboard/view_staff/')



################ attendence staff ################## 
def staff_attendence(request):
    return render(request,"/dashboard/staff_attendence.html")
  
    
