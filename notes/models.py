from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=40)

class Note(models.Model):
    title = models.CharField(max_length=40)
    course = models.ManyToManyField(Courses)
    keycol = models.TextField()
    bodycol = models.TextField()
    pub_date = models.DateTimeField()
    comments_enabled = models.BooleanField()
