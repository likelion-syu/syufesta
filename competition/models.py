from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

Category_select = (
    ('농구', '농구'),
    ('축구', '축구'),
    ('탁구', '탁구'),
)

class Major(models.Model):

    icon = models.ImageField(upload_to='img/')
    intro = models.TextField()
    name = models.CharField(max_length=20)
    slogan = models.CharField(max_length=200, blank=True)

    def sumury(self):
        return self.intro[:10]
    
    def __str__(self):
        return self.name

class Student(models.Model):
    major = models.ForeignKey('competition.Major', related_name='students', on_delete=models.CASCADE)
    student_num = models.CharField(max_length=12)
    age = models.CharField(max_length=4)
    back_num = models.CharField(max_length=4)
    exercise = models.CharField(max_length=20, choices = Category_select, default = '농구')
    stu_name = models.CharField(max_length=100, default='홍길동')

    def __str__(self):
        return self.stu_name

