from pyexpat import model
from django.db import models
# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=25)

class School_Class(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="school_class")
    class_name = models.CharField(max_length=5)

class Class_Section(models.Model):
    school_class = models.ForeignKey(School_Class,on_delete=models.CASCADE,related_name="class_section")
    section_name = models.CharField(max_length=5)