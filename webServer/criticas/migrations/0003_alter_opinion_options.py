# Generated by Django 3.2.8 on 2021-11-18 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criticas', '0002_auto_20211118_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinion',
            options={'ordering': ['nombre'], 'verbose_name': 'Opinion', 'verbose_name_plural': 'Opiniones'},
        ),
    ]
