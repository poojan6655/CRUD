from django.db import models

# Create your models here.
class Admin(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    contactno = models.IntegerField(max_length=15)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Employee(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=20,blank=True)
    contactno = models.IntegerField(max_length=15)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Meeting(models.Model):
    companyname = models.CharField(max_length=20)
    companyaddress = models.CharField(max_length=200)
    contactno = models.IntegerField(max_length=15)
    Contactperson = models.CharField(max_length=20)
    meetingpurpose = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=False,blank=False)
    comments = models.CharField(max_length=200)
    