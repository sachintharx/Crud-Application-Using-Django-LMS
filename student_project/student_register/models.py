from django.db import models

# Create your models here.

class Grade(models.Model):
    grd = models.CharField(max_length=50)
    
    def __str__(self):
        return self.grd 
    


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    
    
     
