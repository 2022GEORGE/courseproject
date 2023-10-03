from django.db import models

# Create your models here.
class coursetable(models.Model):
    fee=models.IntegerField()
    course=models.CharField(max_length=255)
    def __str__(self):
        return self.course
class studenttable(models.Model):
    course_id=models.ForeignKey(coursetable,on_delete=models.CASCADE,null=True,related_name='display')
    name=models.CharField(max_length=255,null=True)
    college=models.CharField(max_length=255,null=True)
    age=models.IntegerField()
    Joining_date=models.DateField()
        
       