# Generated by Django 3.0.6 on 2020-05-25 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voluntarios', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eventos',
            new_name='Evento',
        ),
    ]
