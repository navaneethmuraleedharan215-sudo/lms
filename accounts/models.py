from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from accounts.models import User
from django.db.models.signals import post_save

class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True)

    ROLE_CHOICES=(
        ('admin','admin'),
        ('trainer','trainer'),
        ('student'),('student'),
    )

    role=models.CharField(max_length=200,choices=ROLE_CHOICES,default='student')

    
class TrainerProfile(models.Model):

    trainer = models.OneToOneField(User,on_delete=models.CASCADE,related_name="trainer_profile")

    profile_picture = models.ImageField(upload_to="cover_pics",null=True,blank=True)

    qualification = models.CharField(max_length=200)

    specialization = models.CharField(max_length=200)

    experience = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_data = models.DateTimeField(auto_now=True)


class StudentProfile(models.Model):

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_profile")

    profile_picture = models.ImageField(upload_to="cover_pics",null=True,blank=True)

    skill = models.CharField(max_length=200)

    qualification = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


def create_trainer_profile(sender,instance,create,*args,**kwargs):

    if create and instance.role =="trainer":

        TrainerProfile.objects.create(trainer=instance)

post_save.connect(create_trainer_profile,sender=User)


def create_student_profile(sender,instance,create,*args,**kwargs):

    if create and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)
