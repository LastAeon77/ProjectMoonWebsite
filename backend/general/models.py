from django.db import models


# Create your models here.
class Interview(models.Model):
    name = models.CharField(max_length=30, unique=True)
    body = models.TextField()
    date = models.DateField()
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
