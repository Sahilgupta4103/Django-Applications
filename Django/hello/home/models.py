from django.db import models

# Create your models here.
class Contact(models.Model):
    email= models.EmailField(max_length=122)
    phone= models.CharField(max_length=122)
    
def __str__(self):
    return self.email

