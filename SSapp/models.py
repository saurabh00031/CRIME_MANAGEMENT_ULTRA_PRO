from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser
# Models here...........................................................................................................


#creating multiusers....................................................................................................


class User(AbstractUser):      
    is_user = models.BooleanField(default=False)
    is_crim = models.BooleanField(default=False)
    is_crt = models.BooleanField(default=False)



class criminfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    no_of_cases= models.CharField(max_length=10)
    desc1 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=100) 

    def __str__(self):
        return self.hospital_Name

class usrinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return self.full_Name
    def __str__(self):
        return self.email


class crtinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.full_Name
   
#below users are not multiusers...............................................


class Contact2(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
  

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
   

class imageWale(models.Model):
    pic=models.ImageField(upload_to="profiles")

    


class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    
    


