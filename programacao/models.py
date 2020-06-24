from django.db import models
from voluntarios.models import Voluntario
from PIL import Image

class Programa(models.Model):
    # If the volunteer is deleted the event still remains in the DB
    volunteer = models.ForeignKey(Voluntario, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=200, default="Portuguese")
    program_type = models.CharField(max_length=200)
    program_date = models.DateTimeField(blank=True)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y%m%d/')
    
    def __str__(self):
        return self.title # displays title as the main field in the admin area

    # Resize image automatically
    def save(self, *args, **kwargs):
        # Runs the save method of the parent class
        super().save()

        img = Image.open(self.photo_main.path)
        if img.height > 800 or img.width > 566:
            size = (800, 566)
            img.thumbnail(size)
            img.save(self.photo_main.path)
