from django.db import models
from voluntarios.models import Voluntario
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image

class Livro(models.Model):
    # If the volunteer is deleted the book still remains in the DB
    volunteer = models.ForeignKey(Voluntario, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    medium = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    copies = models.IntegerField(default=1)
    language = models.CharField(max_length=50, default="Portuguese")
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='library/books/%Y_%m_%d/', default='book.jpg', blank=True)

    def __str__(self):
        return self.title # displays title as the main field in the admin area

    # Resize image automatically
    def save(self, *args, **kwargs):
        # Runs the save method of the parent class
        super().save()

        img = Image.open(self.photo_main.path)
        if img.height > 350 or img.width > 255:
            size = (350, 255)
            img.thumbnail(size)
            img.save(self.photo_main.path)

class Reserva(models.Model):
    # If book is deleted, it gets removed from reservation table in the DB
    code = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    checkout_date = models.DateTimeField(default=datetime.now, blank=True)
    return_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True) # Connected to the register user logged in
    
    def __str__(self):
        return self.title