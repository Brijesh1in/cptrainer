from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key = True)
    username = models.CharField("username" , max_length = 30)
    email = models.EmailField("email" , max_length = 50)
    cfhandle = models.CharField("cfhandle" , max_length = 30)
    password = models.CharField("password" , max_length = 30)

# Creating table Problems 
# class Problems(models.Model):
#     pass

# class Submissions(models.Model):
#     pass

# class Recommended(models.Model):
#     pass

'''
Problems:
problemCode
problemLink
rating
tags = *dp*greedy*
date
'''
class Problems(models.Model):
    problemCode = models.CharField(max_length=30)
    rating = models.IntegerField()
    tags = models.CharField(max_length=200)
'''
Recommended_problems
pcode
weeknumber
setNumber
status : 1: accept, -1: reject, 0: untried
startTime =
'''
class RecommendedProblems(models.Model):
    problemCode = models.CharField(max_length=30)
    week = models.IntegerField()
    status = models.IntegerField()
    startTime = models.IntegerField()
'''
Submissions
pcode
status : 1: accept, -1: reject, 0: untried
submissionTime =
'''
class Submissions(models.Model):
    problemCode = models.CharField(max_length=30)
    status = models.IntegerField()
    submissionTime = models.IntegerField()

