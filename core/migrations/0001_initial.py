# Generated by Django 5.0.1 on 2024-02-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesas', models.IntegerField()),
                ('cadeiras', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='nome_completo', max_length=40)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.TextField(max_length=150, verbose_name='Senha')),
                ('imagem', models.ImageField(upload_to='imgs/')),
            ],
        ),
    ]
