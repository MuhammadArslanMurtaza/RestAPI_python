from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError


# Create your models here.

class Employee(models.Model):
     empfname = models.CharField(max_length=20,null=True)
     emplname = models.CharField(max_length=20,default='')
     description = models.TextField(default='')
     createdAt = models.DateTimeField(auto_now_add = True)

     def __str__(self):
          return self.empfname
     objects = models.Manager

     class Meta:
          db_table = 'employee'
          managed = True
          verbose_name = 'Employee'
          verbose_name_plural = 'Employees'

class EmployeeForm(forms.ModelForm):
     class Meta:
          model = Employee
          fields = ['empfname','emplname','description']

     def clean(self):
          data = self.cleaned_data
          keys = list(data.keys())
          print(len(data['empfname'])<10)
          if (len(data['empfname'])<10):
               raise ValidationError("some error in title")
          if (len(data['emplname'])<10):
               raise ValidationError("some error in title")
          if (len(data['description'])<10):
               raise ValidationError("some error in title")

