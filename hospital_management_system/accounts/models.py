from django.db import models

'''
Models are used to define the structure of the database. They are to define the fields and behavior of the data you’re storing in the database.
Syntax:
class ModelName(models.Model):
    field_name = models.FieldType(args)
'''

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField
    password=models.CharField(max_length=200)
    role=models.CharField(choices=(('admin','admin'),('doctor','doctor'),('patient','patient'),('nurse','nurse'),('receptionist','receptionist'),('pharmacist','pharmacist')))

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    profile_picture=models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    
