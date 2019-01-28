from django.db import models

# Create your models here.

class Candidate(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    birthdate = models.DateField('Date of Birth')
    platform = models.TextField()

class Position(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Vote(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField(auto_now_add=True)
