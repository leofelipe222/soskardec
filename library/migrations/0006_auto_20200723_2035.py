# Generated by Django 3.0.6 on 2020-07-23 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200723_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Livro'),
        ),
    ]
