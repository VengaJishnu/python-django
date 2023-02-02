from django.db import models

class todo(models.Model):
    name = models.TextField(max_length=200)
    priority = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.name
# Create your models here.
