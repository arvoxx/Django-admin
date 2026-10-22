from django.db import models

class contact(models.Model):
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=64)
    email= models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()