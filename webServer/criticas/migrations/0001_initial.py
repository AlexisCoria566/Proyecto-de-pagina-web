# Generated by Django 3.2.8 on 2021-11-18 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Usuario')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen de Perfil')),
                ('calificacion', models.ImageField(upload_to='', verbose_name='Calificacion')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
