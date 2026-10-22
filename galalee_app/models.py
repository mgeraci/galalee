from django.db import models

class Show(models.Model):
    location = models.CharField(max_length=200)
