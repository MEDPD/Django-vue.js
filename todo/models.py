from django.db import models

# Create your models here.


class Todoproject(models.Model):
    todo = models.CharField(max_length=30)
