from django.db import models
from user.models import major_tb, user_tb

# Create your models here.

class subject_type_tb(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class subject_tb(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    major = models.ForeignKey(major_tb, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(subject_type_tb, on_delete=models.CASCADE)

class pre_subject_tb(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(subject_tb, on_delete=models.CASCADE)
    pre_subject = models.ForeignKey(subject_tb, on_delete=models.CASCADE)

class complete_tb(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    subject = models.ForeignKey(subject_tb, on_delete=models.CASCADE)
    user = models.ForeignKey(user_tb, on_delete=models.CASCADE)