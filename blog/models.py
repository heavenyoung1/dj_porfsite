from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateField()

    def __str__(self):
        return self.title