from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES=(
        ('ADMIN','Admin'),
        ('TRAINER','Trainer'),
        ('STUDENT'),('Student'),
    )

    name=models.CharField(max_length=150)

    email=models.EmailField(unique=True)

    phone=models.CharField(max_length=15,unique=True)

    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default='STUDENT')

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    
    
class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passoutyear = models.CharField(max_length=20,null=True)

    student=models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class Trainer(models.Model):

    name=models.CharField(max_length=100)

    qualification = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    experience = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
            return self.email