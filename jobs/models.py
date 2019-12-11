from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length= 200)

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return(self.title)

class Social(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return(self.title)

class Skills(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return(self.title)

