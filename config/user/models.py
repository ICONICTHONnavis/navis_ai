from django.db import models

class major_tb(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'major_tb'

class user_tb(models.Model):
    id = models.AutoField(primary_key=True)
    major = models.ForeignKey(major_tb, on_delete=models.CASCADE)
    student_number = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=255)
    admission = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    nl_description = models.TextField(blank=True)

    class Meta:
        db_table = 'user_tb'

 # Create your models here.
