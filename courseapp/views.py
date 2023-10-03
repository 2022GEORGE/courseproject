from django.shortcuts import render,redirect
from courseapp.models import coursetable,studenttable
from django.contrib import messages 
# Create your views here.
def home(request):
    return render(request,'home.html')
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
def addstudent(request):
    data=coursetable.objects.all()
    return render(request,'addstudent.html',{'d':data})
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
        
        
        