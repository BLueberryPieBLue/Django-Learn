from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)




class Zone(models.Model):
    username = models.CharField(max_length=20)
    sendtxt = models.CharField(max_length=255)
    times = models.CharField(max_length=50)
    sendtime = models.CharField(max_length=50)
    photoname = models.FileField(upload_to='photo')
    # musicname = models.FileField(upload_to='music')
