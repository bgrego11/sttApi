
from django.db import models
from django.utils import timezone
# Create your models here.


class Event(models.Model):
    name = models.TextField()
    logdate = models.DateTimeField()
    address = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)


    def __str__(self):
        return self.name