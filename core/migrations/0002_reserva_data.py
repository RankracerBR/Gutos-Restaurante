# Generated by Django 5.0.1 on 2024-02-07 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
