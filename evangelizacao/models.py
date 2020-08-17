from django.db import models
from voluntarios.models import Voluntario
from .validators import validate_file_extension

class Evangelizacao(models.Model):
    # If the volunteer is deleted the event still remains in the DB
    volunteer = models.ForeignKey(Voluntario, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200, default="Portuguese")
    description = models.TextField(blank=True)
    class_date = models.DateTimeField(blank=True)
    class_type = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    doc_file = models.FileField(upload_to="uploads/evangelizacao/%Y_%m_%d/", validators=[validate_file_extension], blank=True)

    def __str__(self):
        return self.title # displays title as the main field in the admin area