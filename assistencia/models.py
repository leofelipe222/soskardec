from django.db import models
from datetime import datetime

class Assistencia(models.Model):
    demmand = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name
