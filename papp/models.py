from django.db import models

# Create your models here.

class pet_usereg(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    dob=models.DateField(max_length=8)
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    ph_no=models.CharField(max_length=50)
    
    def __str__(self):
        return self.f_name

class pet_details(models.Model):
    p_name=models.CharField(max_length=100)
    pet_des=models.CharField(max_length=200)
    p_image=models.CharField(max_length=200)

    def __str__(self):
        return self.p_name