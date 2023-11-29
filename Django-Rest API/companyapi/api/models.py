from django.db import models

# Create your models here.

#creating company model

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=30)
    about=models.CharField(max_length=30)
    type=models.CharField(max_length=100, choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ('Civil','Civil')
                           )
                          )
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + "--" + self.location
    
    
#Employee model    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    number=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(
        ('Manager','mgr'),
        ('Software Developer','sde'),
         ('Project Leader','pl') 
    ))
    
    company=models.ForeignKey(Company,on_delete=models.CASCADE)