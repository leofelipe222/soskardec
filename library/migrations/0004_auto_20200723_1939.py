# Generated by Django 3.0.6 on 2020-07-23 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200723_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='editor',
            new_name='publisher',
        ),
    ]