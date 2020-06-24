from django.db import models
from datetime import datetime
from voluntarios.models import Voluntario
from PIL import Image

# Create your models here.
class Evento(models.Model):
    # If the volunteer is deleted the event still remains in the DB
    volunteer = models.ForeignKey(Voluntario, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y%m%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.title # displays title as the main field in the admin area


    # Resize image automatically
    def save(self, *args, **kwargs):
        # Runs the save method of the parent class
        super().save()

        img = Image.open(self.photo_main.path)
        if img.height > 640 or img.width > 427:
            size = (640, 427)
            img.thumbnail(size)
            img.save(self.photo_main.path)
