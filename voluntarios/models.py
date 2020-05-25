from django.db import models
from datetime import datetime

class Voluntario(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    join_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name

