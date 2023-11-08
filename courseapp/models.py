from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class coursetable(models.Model):
    fee=models.IntegerField()
    course=models.CharField(max_length=255)
class studenttable(models.Model):
    course_id=models.ForeignKey(coursetable,on_delete=models.CASCADE,null=True,related_name='display')
    name=models.CharField(max_length=255,null=True)
    college=models.CharField(max_length=255,null=True)
    age=models.IntegerField()
    Joining_date=models.DateField()
class usertable(models.Model):
    course=models.ForeignKey(coursetable,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,null=True)
    age=models.IntegerField()
    contact=models.CharField(max_length=255)
    image=models.FileField(upload_to='images',null=True)    
        
       