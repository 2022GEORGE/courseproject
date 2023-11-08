from django.shortcuts import render,redirect
from courseapp.models import coursetable,studenttable,usertable
from django.contrib import messages 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def welcome(request):
    return render(request,'login.html')
@login_required(login_url='welcome')
def home(request):
    return render(request,'home.html')
@login_required(login_url='welcome')
def addcourse(request):
    return render(request,'addcourse.html')
def add(request):
    if request.method=='POST':
        name=request.POST['fee']
        cname=request.POST['course']
        if coursetable.objects.filter(course=cname).exists():
            messages.warning(request,'THE COURSE ALREADY EXISTS')
            return redirect('addcourse')
        else:
            data=coursetable(fee=name,course=cname)
            data.save()
            messages.success(request,'THE COURSE ADD SUCCESFULLY')
            return redirect('addcourse')
    return redirect('addcourse')
@login_required(login_url='welcome')
def addstudent(request):
    data=coursetable.objects.all()
    return render(request,'addstudent.html',{'d':data})
@login_required(login_url='welcome')
def details(request):
    data=studenttable.objects.all()
    return render(request,'table.html',{'k':data})
def addstudentdb(request):
    if request.method=='POST':
        s_name=request.POST['name']
        s_address=request.POST['college']
        s_age=request.POST['age']
        s_date=request.POST['date']
        sel=request.POST['course']
        s_course=coursetable.objects.get(id=sel)
        data=studenttable(name=s_name,college=s_address,age=s_age,Joining_date=s_date,course_id=s_course)
        data.save()
        messages.success(request,' ADD STUDENT SUCCESFULLY')
        return redirect('addstudent')
    return redirect('addcourse')
@login_required(login_url='welcome')
def editpage(request,pk):
    data=coursetable.objects.all()
    student=studenttable.objects.get(id=pk)
    return render(request,'edit.html',{'d':data,'st':student})
def edit(request,pk):
    if request.method=='POST':
       student=studenttable.objects.get(id=pk)
       student.name=request.POST['name']
       student.college=request.POST['college']
       student.age=request.POST['age']
       student.Joining_date=request.POST['date']
       sel=request.POST['course']
       student.course_id=coursetable.objects.get(id=sel)
       student.save()
       return redirect('details')
    return redirect('editage')
def delt(request,pk):
    data=studenttable.objects.get(id=pk)
    data.delete()
    return redirect('details')        
def loginfun(request):
    if request.method =='POST':
        name=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                login(request,user)
                current=request.user.id
                data=User.objects.get(id=current)
                subject="LOGIN DETECTED"
                message="LOGIN TIME "+str(data.last_login)
                send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
                messages.info(request,f'Welcome {name}')
                return redirect('teacher')
        else:
            messages.info(request,"INVALID USER NAME OR PASSWORD")
            return redirect('welcome')
    else:
        return redirect('welcome')
@login_required(login_url='welcome')      
def logout(request):
    auth.logout(request)
    return redirect('welcome')
def signup(request):
    data=coursetable.objects.all()
    return render(request,'signup.html',{'data':data})
def addteacher(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        uemail=request.POST['email']
        uage=request.POST['age']
        ucontact=request.POST['number']
        sel=request.POST['sel']
        image=request.FILES.get('image')
        course=coursetable.objects.get(id=sel)
        if password ==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"USER NAME ALREADY EXIST")
                return redirect('signup')
            else:
                data=User.objects.create_user( first_name=fname,last_name=lname,username=uname,password=password,email=uemail)
                data.save()
                
                udata=usertable(address=address,age=uage,contact=ucontact,image=image,user=data,course=course)
                udata.save()
                subject="REGISTRATION SUCCESSFULL"
                message="Hi "+fname+" your profile account has created \n userid="+uname+"\n password="+password
                send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
                return redirect('welcome')
        else:
            messages.info(request,"PASSWORD AND CONFORM PASSWORD MUST BE SAME")
            return redirect('signup') 
    else:
        return redirect('signup')
@login_required(login_url='welcome')    
def teacher(request):
    return render(request,'teacher.html')
@login_required(login_url='welcome')    
def teacherdetails(request):
    data=User.objects.all()
    userd=usertable.objects.all()
    return render(request,'teacherdetails.html',{'data':data,'user':userd})
def dele(request,pk):
    u=usertable.objects.get(user=pk)
    u.delete()
    d=User.objects.get(id=pk)
    d.delete()
    return redirect('teacherdetails')
@login_required(login_url='welcome')
def profile(request):
    current=request.user.id
    data=usertable.objects.get(user=current)
    return render(request,'profile.html',{'d':data})           
@login_required(login_url='welcome')        
def teacheredit(request):
    current=request.user.id
    data=usertable.objects.get(user=current)
    c=coursetable.objects.all()
    return render(request,'teacheredit.html',{'d':data,'cu':c})       
def updatedb(request,pk):
    if request.method =='POST':
        data=User.objects.get(id=pk)
        data.first_name=request.POST['fname']
        data.last_name=request.POST['lname']
        data.username=request.POST['username']
        data.email=request.POST['email']
        data.save()
        udata=usertable.objects.get(user=pk)        
        udata.address=request.POST['address']
        udata.age=request.POST['age']
        udata.contact=request.POST['number']
        udata.user=data
        courseid=request.POST['sel']
        udata.course=coursetable.objects.get(id=courseid)
        if len(request.FILES)!=0:
            if len(udata.image)>0:
                os.remove(udata.image.path)
            udata.image=request.FILES.get('image')
        udata.save()
        subject="profile updated"
        message="Hi "+str(data.first_name)+" your profile updated "
        send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
        return redirect('profile')
    return redirect('teacheredit')