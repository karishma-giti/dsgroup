from django.shortcuts import render, redirect  
from django.http import HttpResponse,HttpResponseRedirect
from .models import Intern,Staff,Trainee  




# ###################intern#####################

def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def register_intern(request):
    interns = Intern(request.POST,request.FILES)
    if request.method =="POST":
        intern_id=request.POST.get('intern_id')
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
        school_marksheet=request.FILES.get('school_marksheet')

        high_school_name=request.POST.get('high_school_name')
        high_school_board=request.POST.get('high_school_board')
        high_school_passing_year=request.POST.get('high_school_passing_year')
        high_school_marksheet=request.FILES.get('high_school_marksheet')

        graduation_univercity=request.POST.get('graduation_univercity')
        graduation_degree=request.POST.get('graduation_degree')
        graduation_year=request.POST.get('graduation_year')
        graduation_marksheet=request.FILES.get('graduation_marksheet')

        
        post_graduation_univercity=request.POST.get('post_graduation_univercity')
        post_graduation_degree=request.POST.get('post_graduation_degree')
        post_graduation_year=request.POST.get('post_graduation_year')
        post_graduation_marksheet=request.FILES.get('post_graduation_marksheet')

       
        other_univercity =request.POST.get('other_univercity')
        other_degree=request.POST.get('other_degree')
        other_year=request.POST.get('other_year')
        other_marksheet=request.FILES.get('other_marksheet')

        Insertion=Intern(intern_id=intern_id,profile=profile, intern_name= intern_name,email=email, phone_no= phone_no, aadhar_no= aadhar_no,
        pan_card=pan_card,gender=gender,date_of_birth=date_of_birth,blood_group=blood_group,father_name=father_name,
        father_occupation=father_occupation,father_no=father_no,city=city,pin_code=pin_code,address=address,join_date=join_date
        ,school_name=school_name,board=board, passing_year=passing_year,school_marksheet=school_marksheet,high_school_name=high_school_name
        ,high_school_board=high_school_board,high_school_passing_year=high_school_passing_year,high_school_marksheet=high_school_marksheet,
        graduation_univercity=graduation_univercity,graduation_degree=graduation_degree, graduation_year= graduation_year,
        graduation_marksheet=graduation_marksheet,post_graduation_degree=post_graduation_degree,post_graduation_univercity=post_graduation_univercity
        ,post_graduation_year=post_graduation_year,post_graduation_marksheet=post_graduation_marksheet,
        other_degree=other_degree,other_univercity=other_univercity,other_year=other_year,other_marksheet=other_marksheet,state=state)
        Insertion.save()
        return render(request,"dashboard/register_intern.html")
    else:
        return render(request,"dashboard/register_intern.html")

def view_interns(request):
    data = Intern(request.GET)
    interns = Intern.objects.all()
    print(interns)
    return render(request,"dashboard/view_intern.html",{'view_intern':interns} )
    
    

def intern_profile(request,id):
    interns = Intern.objects.filter(id=id)
    print(interns)
    return render(request,"dashboard/intern_profile.html")
    

def interns_attendence(request):
    return render(request,"dashboard/intern_attendence.html")

def edit_intern(request,id):
    interns = Intern.objects.get(id=id)
    print(interns)
    return render(request,"dashboard/edit_intern.html",{'edit_intern':interns})    

def manage_intern(request,id):
    interns = Intern.objects.get(id=id) 
    if request.method =="POST":
        interns.intern_id=request.POST.get('intern_id','')
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
        if "school_marksheet" in request.FILES:
            img=request.FILES["school_marksheet"]
            interns.school_marksheet =img
        interns.save()

        interns.high_school_name=request.POST.get('high_school_name','')
        interns.high_school_board=request.POST.get('high_school_board','')
        interns.high_school_passing_year=request.POST.get('high_school_passing_year','')
        if "high_school_marksheet" in request.FILES:
            img=request.FILES["employee_photo"]
            interns.high_school_marksheet =img
        interns.save()

        interns.graduation_univercity=request.POST.get('graduation_univercity','')
        interns.graduation_degree=request.POST.get('graduation_degree','')
        interns.graduation_year=request.POST.get('graduation_year','')
        if "graduation_marksheet" in request.FILES:
            img=request.FILES["graduation_marksheet"]
            graduation_marksheet.graduation_marksheet =img
        interns.save()

        
        interns.post_graduation_univercity=request.POST.get('post_graduation_univercity','')
        interns.post_graduation_degree=request.POST.get('post_graduation_degree','')
        interns.post_graduation_year=request.POST.get('post_graduation_year','')
        if "post_graduation_marksheet" in request.FILES:
            img=request.FILES["post_graduation_marksheet"]
            interns.post_graduation_marksheet =img
        interns.save()

       
        interns.other_univercity =request.POST.get('other_univercity','')
        interns.other_degree=request.POST.get('other_degree','')
        interns.other_year=request.POST.get('other_year','')
        if "other_marksheet" in request.FILES:
            img=request.FILES["other_marksheet"]
            interns.employee_photo =img
        interns.save()
    return redirect('/dashboard/view_interns')


def remove_intern(request):
    Id=request.POST['inter_id']
    print(Id)
    interns = Intern.objects.get(pk=Id)
    interns.delete()
    return redirect('/dashboard/view_interns')       

# ###################traninees#####################

def register_trainees(request):
    trainee = Trainee(request.POST,request.FILES)
    if request.method =="POST":
        trainee_id=request.POST.get('trainee_id')
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
        school_marksheet=request.FILES.get('school_marksheet')

        high_school_name=request.POST.get('high_school_name')
        high_school_board=request.POST.get('high_school_board')
        high_school_passing_year=request.POST.get('high_school_passing_year')
        high_school_marksheet=request.FILES.get('high_school_marksheet')

        graduation_univercity=request.POST.get('graduation_univercity')
        graduation_degree=request.POST.get('graduation_degree')
        graduation_year=request.POST.get('graduation_year')
        graduation_marksheet=request.FILES.get('graduation_marksheet')

        
        post_graduation_univercity=request.POST.get('post_graduation_univercity')
        post_graduation_degree=request.POST.get('post_graduation_degree')
        post_graduation_year=request.POST.get('post_graduation_year')
        post_graduation_marksheet=request.FILES.get('post_graduation_marksheet')

       
        other_univercity =request.POST.get('other_univercity')
        other_degree=request.POST.get('other_degree')
        other_year=request.POST.get('other_year')
        other_marksheet=request.FILES.get('other_marksheet')

        Insertion=Trainee(trainee_id=trainee_id,profile=profile, trainee_name= trainee_name,email=email, phone_no= phone_no, aadhar_no= aadhar_no,
        pan_card=pan_card,gender=gender,date_of_birth=date_of_birth,blood_group=blood_group,father_name=father_name,
        father_occupation=father_occupation,father_no=father_no,city=city,pin_code=pin_code,address=address,join_date=join_date
        ,school_name=school_name,board=board, passing_year=passing_year,school_marksheet=school_marksheet,high_school_name=high_school_name
        ,high_school_board=high_school_board,high_school_passing_year=high_school_passing_year,high_school_marksheet=high_school_marksheet,
        graduation_univercity=graduation_univercity,graduation_degree=graduation_degree, graduation_year= graduation_year,
        graduation_marksheet=graduation_marksheet,post_graduation_degree=post_graduation_degree,post_graduation_univercity=post_graduation_univercity
        ,post_graduation_year=post_graduation_year,post_graduation_marksheet=post_graduation_marksheet,
        other_degree=other_degree,other_univercity=other_univercity,other_year=other_year,other_marksheet=other_marksheet,state=state)
        Insertion.save()
        return render(request,"dashboard/register_trainees.html")
    else:
        return render(request,"dashboard/register_trainees.html")

def view_trainees(request):
    data = Trainee(request.GET)
    trainees = Trainee.objects.all()
    print(trainees)
    return render(request,"dashboard/view_trainees.html",{'view_trainees':trainees} )


# def trainees_profile(request,id):
#     interns = Intern.objects.filter(id=id)
#     print(interns)
#     return render(request,"dashboard/intern_profile.html")
        


def edit_trainees(request,id):
    trainees = Trainee.objects.get(id=id)
    print(trainees)
    return render(request,"dashboard/edit_trainees.html",{'edit_trainees':trainees})    

def manage_trainees(request,id):
    trainees = Trainee.objects.get(id=id) 
    if request.method =="POST":
        trainees.trainee_id=request.POST.get('trainee_id','')
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
        if "school_marksheet" in request.FILES:
            img=request.FILES["school_marksheet"]
            trainees.school_marksheet =img
        trainees.save()

        trainees.high_school_name=request.POST.get('high_school_name','')
        trainees.high_school_board=request.POST.get('high_school_board','')
        trainees.high_school_passing_year=request.POST.get('high_school_passing_year','')
        if "high_school_marksheet" in request.FILES:
            img=request.FILES["employee_photo"]
            trainees.high_school_marksheet =img
        trainees.save()

        trainees.graduation_univercity=request.POST.get('graduation_univercity','')
        trainees.graduation_degree=request.POST.get('graduation_degree','')
        trainees.graduation_year=request.POST.get('graduation_year','')
        if "graduation_marksheet" in request.FILES:
            img=request.FILES["graduation_marksheet"]
            trainees.graduation_marksheet =img
        trainees.save()

        
        trainees.post_graduation_univercity=request.POST.get('post_graduation_univercity','')
        trainees.post_graduation_degree=request.POST.get('post_graduation_degree','')
        trainees.post_graduation_year=request.POST.get('post_graduation_year','')
        if "post_graduation_marksheet" in request.FILES:
            img=request.FILES["post_graduation_marksheet"]
            trainees.post_graduation_marksheet =img
        trainees.save()

       
        trainees.other_univercity =request.POST.get('other_univercity','')
        trainees.other_degree=request.POST.get('other_degree','')
        trainees.other_year=request.POST.get('other_year','')
        if "other_marksheet" in request.FILES:
            img=request.FILES["other_marksheet"]
            trainees.employee_photo =img
        trainees.save()
    return redirect('/dashboard/view_trainees')

def remove_trainees(request):
    Id=request.POST['trainee_id']
    print(Id)
    trainees = Trainee.objects.get(pk=Id)
    trainees.delete()
    return redirect('/dashboard/view_trainees')       




def trainees_attendence(request):
    return render(request,"dashboard/trainees_attendence.html")

####################employee#####################    

def register_employees(request):
    return render(request,"dashboard/register_employees.html")

def view_employees(request):
    return render(request,"dashboard/view_employees.html")

def employees_attendence(request):
    return render(request,"dashboard/employees_attendence.html")


####################payrol#####################  

# payroll

def add_salary(request):
    return render(request,"dashboard/add_salary.html")

def view_salary(request):
    return render(request,"dashboard/view_salary.html")


####################employee#####################  

def register_staff(request):
    if request.method =="POST":
        print(request.POST)
        staff_id=request.POST['staff_id']
        staff_name=request.POST['staff_name']
        phone_no=request.POST['phone_no']
        aadhar_no=request.POST['aadhar_no']
        role=request.POST['role']
        join_date=request.POST['join_date']

        Insertion=Staff(staff_id=staff_id,staff_name=staff_name, phone_no= phone_no,aadhar_no=aadhar_no,role=role,join_date=join_date)
        Insertion.save()
        return render(request,"dashboard/register_staff.html")
    else:
        return render(request,"dashboard/register_staff.html")
    
       
def view_staff(request):
    data = Staff.objects.all()
    return render(request,"dashboard/view_staff.html",{'data':data})

def delete_staff(request, id):
    staff=Staff.objects.filter(pk=id)
    staff.delete()
    return HttpResponseRedirect("/dashboard/view_staff")


def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    print(staff)
    return render(request,"dashboard/edit_staff.html",{'staff':staff})

def manage_staff(request,id):
    staff = Staff.objects.get(id=id)
    if request.method == "POST":
        staff.staff_id = request.POST.get('staff_id','') 
        staff.staff_name = request.POST.get('staff_name','') 
        staff.phone_no = request.POST.get('phone_no','')
        staff.aadhar_no = request.POST.get('aadhar_no','')
        staff.role = request.POST.get('role','')
        staff.join_date = request.POST.get('join_date','')
        staff.save()
    return redirect('/dashboard/view_staff/')

def staff_attendence(request):
    return render(request,"dashboard/staff_attendence.html")
