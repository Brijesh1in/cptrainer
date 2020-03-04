from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key = True)
    username = models.CharField("username" , max_length = 30)
    email = models.EmailField("email" , max_length = 50)
    cfhandle = models.CharField("cfhandle" , max_length = 30)
    password = models.CharField("password" , max_length = 30)

# Creating table Problems 
class Problems(models.Model):
    pass

class Submissions(models.Model):
    pass

class Recommended(models.Model):
    pass

