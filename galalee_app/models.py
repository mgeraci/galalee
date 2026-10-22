from django.db import models

class Show(models.Model):
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return '{}, {}'.format(self.venue, self.date)