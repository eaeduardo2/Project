from django.db import models
from django.utils import timezone


class Post(models.Model):
    Email = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Grade = models.CharField(max_length=50)
    Experience = models.TextField()
    Guardian = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Class = models.CharField(max_length=50)



    def publish(self):
        self.save()

    def __str__(self):
        return self.Name