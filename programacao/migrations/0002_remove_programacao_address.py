# Generated by Django 3.0.6 on 2020-06-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacao',
            name='address',
        ),
    ]
