from django.db import models

# Create your models here.

class Snippet(models.Model):
    name = models.CharField(max_length=60)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.name