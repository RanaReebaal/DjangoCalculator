from django.db import models

# Create your models here.


class School(models.Model):
    Name                = models.CharField(max_length=50 ,default="")
    Father_name         = models.CharField(max_length=50 ,default="")
    Gender              = models.CharField(max_length=50 ,default="")
    Class               = models.CharField(max_length=50 ,default="")
    Section             = models.CharField(max_length=50 ,default="") 
    Roll_No             = models.CharField(max_length=50 ,default="")
    Photo = models.ImageField(upload_to="myimage")
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name


class information(models.Model):
    name                = models.CharField(max_length=50 ,default="")
    father_name         = models.CharField(max_length=50 ,default="")
    gender              = models.CharField(max_length=50 ,default="")
    email               = models.CharField(max_length=50 ,default="")
    password            = models.CharField(max_length=50 ,default="")
    file = models.ImageField(upload_to="myimage")
    def __str__(self):
        return self.name
    


