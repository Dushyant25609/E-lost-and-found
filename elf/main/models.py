from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=200)
    enrolment_no = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)

    
class Organization(models.Model):
    Organisation_name = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
