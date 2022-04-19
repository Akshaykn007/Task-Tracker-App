from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Team(models.Model):
    name = models.CharField(max_length=30)
    teamId=models.IntegerField(max_length=30,null=True,unique=True)
    def __str__(self):
        return str(self.teamId)
        
class Members(models.Model):
    member = models.CharField(max_length=30)
    userId = models.IntegerField(max_length=30,null=True)
    availability=models.BooleanField(max_length=10,null=True)
    email = models.EmailField(max_length=30,null=True)
    def __str__(self):
        return str(self.member)

class TeamMembers(models.Model):
    member= models.CharField(max_length=30)
    team_id= models.IntegerField(max_length=30,null=True)
    def __str__(self):
        return str(self.member)

class Task(models.Model):
    task_name = models.CharField(max_length=30,blank=True)
    task_id = models.IntegerField(max_length=30,null=True)
    priority=models.CharField(max_length=30,blank=True)
    start_date=models.DateField(max_length=30,blank=True)
    end_date=models.DateField(max_length=30,blank=True)
    team_member=models.CharField(max_length=30,blank=True)
    status = models.CharField(max_length=30,blank=True)
    updated_on=models.DateField(max_length=30,blank=True,null=True)
    def __str__(self):
        return str(self.task_id)




